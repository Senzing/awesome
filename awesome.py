#! /usr/bin/env python3

# -----------------------------------------------------------------------------
# awesome.py
#
# References:
# - GitHub
#   - https://github.com/PyGithub/PyGithub
#   - https://pygithub.readthedocs.io/
#   - https://pygithub.readthedocs.io/en/latest/github_objects.html
# -----------------------------------------------------------------------------

import argparse
import json
import linecache
import logging
import os
import signal
import sys
import time
from github import Github
import github

__all__ = []
__version__ = "1.0.0"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = '2020-06-30'
__updated__ = '2021-01-08'

PRODUCT_ID = "5016"
log_format = '%(asctime)s %(message)s'

# The "configuration_locator" describes where configuration variables are in:
# 1) Command line options, 2) Environment variables, 3) Configuration files, 4) Default values

configuration_locator = {
    "debug": {
        "default": False,
        "env": "GITHUB_DEBUG",
        "cli": "debug"
    },
    "github_access_token": {
        "default": None,
        "env": "GITHUB_ACCESS_TOKEN",
        "cli": "github-access-token"
    },
    "organization": {
        "default": "Senzing",
        "env": "GITHUB_ORGANIZATION",
        "cli": "organization"
    },
    "subcommand": {
        "default": None,
        "env": "GITHUB_SUBCOMMAND",
    }
}

# Enumerate keys in 'configuration_locator' that should not be printed to the log.

keys_to_redact = [
    "github_access_token",
]

# -----------------------------------------------------------------------------
# Name mapping.
# -----------------------------------------------------------------------------

awesome_topics = {
    "documentation": {
        "title": "Documentation",
        "description": "Documentation on Senzing usage.",
        "members": [
            {
                "name": "Promoted articles",
                "url": "https://senzing.zendesk.com/hc/en-us",
                "description": "Promoted articles."
            }, {
                "name": "Senzing API for Developers",
                "url": "https://senzing.zendesk.com/hc/en-us/categories/360000120514-Senzing-API-for-Developers-",
                "description": "Senzing API for Developers."
            }, {
                "name": "Tags used in GitHub",
                "url": "https://github.com/Senzing/knowledge-base/blob/master/lists/github-tags-used.md",
                "description": "GitHub tags for Senzing artifacts."
            }
        ]
    },
    "demonstration": {
        "title": "Demonstrations",
        "description": "Step-by-step instructions demonstrating use of Senzing.",
        "members": []
    },
    "dockerfile": {
        "title": "Dockerfiles",
        "description": "Repositories with Dockerfiles.",
        "members": []
    },
    "docker-hub": {
        "title": "DockerHub",
        "description": "Git repositories with Docker images on [DockerHub](https://hub.docker.com/r/senzing/).",
        "members": []
    },
    "docker-compose": {
        "title": "docker-compose",
        "description": "Docker formations using docker-compose.",
        "members": []
    },
    "kubernetes": {
        "title": "Kubernetes",
        "description": "Step-by-step instructions demonstrating use of Senzing on kubernetes-based systems.",
        "members": []
    },
    "helm-chart": {
        "title": "Helm Charts",
        "description": "Git repositories with Helm Charts for Senzing on kubernetes-based systems.",
        "members": []
    },
    "mapper": {
        "title": "Mapper",
        "description": "Convert industry standard formats to Senzing-ready format.",
        "members": []
    },
    "proof-of-concept": {
        "title": "Proof of Concept",
        "description": "Tools to work with Proof of Concept engagements.",
        "members": []
    },
    "resource": {
        "title": "Resources",
        "description": "Non-code information.",
        "members": []
    },
    "ui-component": {
        "title": "User Interface",
        "description": "User interfaces for Senzing.",
        "members": []
    },
    "utility": {
        "title": "Utilities",
        "description": "Tools for working with Senzing.",
        "members": []
    },
    "under-construction": {
        "title": "Under construction",
        "description": "Being worked on. a.k.a. Fresh meat.",
        "members": []
    },
    "obsolete": {
        "title": "Obsolete",
        "description": "Although no longer current, may be informative.",
        "members": []
    },
}

prolog_lines = [
    "# awesome",
    "",
    "Curated list of awesome Senzing software and resources.",
    "Inspired by [other awesome sites](#other-awesome-sites).",
    "",
    "## Contents",
    "",
    "1. [Documentation](#documentation)",
    "1. [Demonstrations](#demonstrations)",
    "1. Docker",
    "    1. [Dockerfiles](#dockerfiles)",
    "    1. [DockerHub](#dockerhub)",
    "    1. [docker-compose](#docker-compose)",
    "    1. [Kubernetes](#kubernetes)",
    "    1. [Helm Charts](#helm-charts)",
    "1. [Mapper](#mapper)",
    "1. [Proof of Concept](#proof-of-concept)",
    "1. [Resources](#resources)",
    "1. [User Interface](#user-interface)",
    "1. [Utilities](#utilities)",
    "1. [Under construction](#under-construction)",
    "1. [Obsolete](#obsolete)",
    "1. [Features and bugs](#features-and-bugs)",
    "1. [Other awesome sites](#other-awesome-sites)",
]

epilog_lines = [
    "",
    "## Features and bugs",
    "",
    "*How to request new features and bug fixes.*",
    "",
    "1. [Request bug fix](https://github.com/Senzing/knowledge-base/blob/master/HOWTO/request-bug-fix.md)",
    "1. [Request new feature in existing repository](https://github.com/Senzing/knowledge-base/blob/master/HOWTO/request-new-feature-in-existing-repository.md)",
    "1. [Request new feature](https://github.com/Senzing/knowledge-base/blob/master/HOWTO/request-new-feature.md)",
    "",
    "## Other awesome sites",
    "",
    "*Our thanks to those who blazed the 'awesome' trail before us.*",
    "",
    "- General:",
    "  [sindresorhus/awesome](https://github.com/sindresorhus/awesome),",
    "- GoLang:",
    "  [avelino/awesome-go](https://github.com/avelino/awesome-go)",
    "- Java:",
    "  [java-lang/awesome-java](https://github.com/java-lang/awesome-java),",
    "  [akullpp/awesome-java](https://github.com/akullpp/awesome-java),",
    "  [awesome-java](https://github.com/uhub/awesome-java)",
    "- JavaScript:",
    "  [sorrycc/awesome-javascript](https://github.com/sorrycc/awesome-javascript),",
    "  [uhub/awesome-javascript](https://github.com/uhub/awesome-javascript)",
    "- PHP:",
    "  [https://github.com/uhub/awesome-php](https://github.com/uhub/awesome-php),",
    "  [ziadoz/awesome-php](https://github.com/ziadoz/awesome-php)",
    "- Python:",
    "  [vinta/awesome-python](https://github.com/vinta/awesome-python)",
]

# -----------------------------------------------------------------------------
# Define argument parser
# -----------------------------------------------------------------------------


def get_parser():
    ''' Parse commandline arguments. '''

    subcommands = {
        'awesome-groups': {
            "help": 'Print awesome groups.',
            "argument_aspects": ["github"],
        },
        'awesome-page': {
            "help": 'Create the awesome page.',
            "argument_aspects": ["github"],
        },
        'awesome-page-excluded': {
            "help": 'List repositories that are not on Awesome page.',
            "argument_aspects": ["github"],
        },
        'version': {
            "help": 'Print version of program.',
        },
    }

    # Define argument_aspects.

    argument_aspects = {
        "github": {
            "--github-access-token": {
                "dest": "github_access_token",
                "metavar": "GITHUB_ACCESS_TOKEN",
                "help": "GitHub Personal Access token. See https://github.com/settings/tokens"
            },
            "--debug": {
                "dest": "debug",
                "action": "store_true",
                "help": "Enable debugging. (GITHUB_DEBUG) Default: False"
            },
            "--organization": {
                "dest": "organization",
                "metavar": "GITHUB_ORGANIZATION",
                "help": "GitHub account/organization name. Default: Senzing"
            },
        },
    }

    # Augment "subcommands" variable with arguments specified by aspects.

    for subcommand, subcommand_value in subcommands.items():
        if 'argument_aspects' in subcommand_value:
            for aspect in subcommand_value['argument_aspects']:
                if 'arguments' not in subcommands[subcommand]:
                    subcommands[subcommand]['arguments'] = {}
                arguments = argument_aspects.get(aspect, {})
                for argument, argument_value in arguments.items():
                    subcommands[subcommand]['arguments'][argument] = argument_value

    parser = argparse.ArgumentParser(prog="github-tasks.py", description="Reports from GitHub.")
    subparsers = parser.add_subparsers(dest='subcommand', help='Subcommands (GITHUB_SUBCOMMAND):')

    for subcommand_key, subcommand_values in subcommands.items():
        subcommand_help = subcommand_values.get('help', "")
        subcommand_arguments = subcommand_values.get('arguments', {})
        subparser = subparsers.add_parser(subcommand_key, help=subcommand_help)
        for argument_key, argument_values in subcommand_arguments.items():
            subparser.add_argument(argument_key, **argument_values)

    return parser

# -----------------------------------------------------------------------------
# Message handling
# -----------------------------------------------------------------------------

# 1xx Informational (i.e. logging.info())
# 3xx Warning (i.e. logging.warning())
# 5xx User configuration issues (either logging.warning() or logging.err() for Client errors)
# 7xx Internal error (i.e. logging.error for Server errors)
# 9xx Debugging (i.e. logging.debug())


MESSAGE_INFO = 100
MESSAGE_WARN = 300
MESSAGE_ERROR = 700
MESSAGE_DEBUG = 900

message_dictionary = {
    "100": "github-" + PRODUCT_ID + "{0:04d}I",
    "101": "Added   Repository: {0} Label: {1}",
    "102": "Updated Repository: {0} Label: {1}",
    "103": "Deleted Repository: {0} Label: {1}",
    "104": "Repository '{0}' has been archived.  Not modifying its labels.",
    "293": "For information on warnings and errors, see https://github.com/docktermj/python-github",
    "295": "Sleeping infinitely.",
    "296": "Sleeping {0} seconds.",
    "297": "Enter {0}",
    "298": "Exit {0}",
    "299": "{0}",
    "300": "github-" + PRODUCT_ID + "{0:04d}W",
    "499": "{0}",
    "500": "github-" + PRODUCT_ID + "{0:04d}E",
    "696": "Bad GITHUB_SUBCOMMAND: {0}.",
    "697": "No processing done.",
    "698": "Program terminated with error.",
    "699": "{0}",
    "700": "github-" + PRODUCT_ID + "{0:04d}E",
    "701": "GITHUB_ACCESS_TOKEN is required",
    "899": "{0}",
    "900": "github-" + PRODUCT_ID + "{0:04d}D",
    "999": "{0}",
}


def message(index, *args):
    index_string = str(index)
    template = message_dictionary.get(index_string, "No message for index {0}.".format(index_string))
    return template.format(*args)


def message_generic(generic_index, index, *args):
    index_string = str(index)
    return "{0} {1}".format(message(generic_index, index), message(index, *args))


def message_info(index, *args):
    return message_generic(MESSAGE_INFO, index, *args)


def message_warning(index, *args):
    return message_generic(MESSAGE_WARN, index, *args)


def message_error(index, *args):
    return message_generic(MESSAGE_ERROR, index, *args)


def message_debug(index, *args):
    return message_generic(MESSAGE_DEBUG, index, *args)


def get_exception():
    ''' Get details about an exception. '''
    exception_type, exception_object, traceback = sys.exc_info()
    frame = traceback.tb_frame
    line_number = traceback.tb_lineno
    filename = frame.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, line_number, frame.f_globals)
    return {
        "filename": filename,
        "line_number": line_number,
        "line": line.strip(),
        "exception": exception_object,
        "type": exception_type,
        "traceback": traceback,
    }

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------


def get_configuration(args):
    ''' Order of precedence: CLI, OS environment variables, INI file, default. '''
    result = {}

    # Copy default values into configuration dictionary.

    for key, value in list(configuration_locator.items()):
        result[key] = value.get('default', None)

    # "Prime the pump" with command line args. This will be done again as the last step.

    for key, value in list(args.__dict__.items()):
        new_key = key.format(subcommand.replace('-', '_'))
        if value:
            result[new_key] = value

    # Copy OS environment variables into configuration dictionary.

    for key, value in list(configuration_locator.items()):
        os_env_var = value.get('env', None)
        if os_env_var:
            os_env_value = os.getenv(os_env_var, None)
            if os_env_value:
                result[key] = os_env_value

    # Copy 'args' into configuration dictionary.

    for key, value in list(args.__dict__.items()):
        new_key = key.format(subcommand.replace('-', '_'))
        if value:
            result[new_key] = value

    # Special case: subcommand from command-line

    if args.subcommand:
        result['subcommand'] = args.subcommand

    # Special case: Change boolean strings to booleans.

    booleans = [
        'debug',
    ]
    for boolean in booleans:
        boolean_value = result.get(boolean)
        if isinstance(boolean_value, str):
            boolean_value_lower_case = boolean_value.lower()
            if boolean_value_lower_case in ['true', '1', 't', 'y', 'yes']:
                result[boolean] = True
            else:
                result[boolean] = False

    # Special case: Change integer strings to integers.

    integers = []
    for integer in integers:
        integer_string = result.get(integer)
        result[integer] = int(integer_string)

    return result


def validate_configuration(config):
    ''' Check aggregate configuration from commandline options, environment variables, config files, and defaults. '''

    user_warning_messages = []
    user_error_messages = []

    # Perform subcommand specific checking.

    subcommand = config.get('subcommand')

    if subcommand in ['comments']:

        if not config.get('github_access_token'):
            user_error_messages.append(message_error(701))

    # Log warning messages.

    for user_warning_message in user_warning_messages:
        logging.warning(user_warning_message)

    # Log error messages.

    for user_error_message in user_error_messages:
        logging.error(user_error_message)

    # Log where to go for help.

    if len(user_warning_messages) > 0 or len(user_error_messages) > 0:
        logging.info(message_info(293))

    # If there are error messages, exit.

    if len(user_error_messages) > 0:
        exit_error(697)


def redact_configuration(config):
    ''' Return a shallow copy of config with certain keys removed. '''
    result = config.copy()
    for key in keys_to_redact:
        result.pop(key)
    return result

# -----------------------------------------------------------------------------
# Utility functions
# -----------------------------------------------------------------------------


def create_signal_handler_function(args):
    ''' Tricky code.  Uses currying technique. Create a function for signal handling.
        that knows about "args".
    '''

    def result_function(signal_number, frame):
        logging.info(message_info(298, args))
        sys.exit(0)

    return result_function


def bootstrap_signal_handler(signal, frame):
    sys.exit(0)


def entry_template(config):
    ''' Format of entry message. '''
    debug = config.get("debug", False)
    config['start_time'] = time.time()
    if debug:
        final_config = config
    else:
        final_config = redact_configuration(config)
    config_json = json.dumps(final_config, sort_keys=True)
    return message_info(297, config_json)


def exit_template(config):
    ''' Format of exit message. '''
    debug = config.get("debug", False)
    stop_time = time.time()
    config['stop_time'] = stop_time
    config['elapsed_time'] = stop_time - config.get('start_time', stop_time)
    if debug:
        final_config = config
    else:
        final_config = redact_configuration(config)
    config_json = json.dumps(final_config, sort_keys=True)
    return message_info(298, config_json)


def exit_error(index, *args):
    ''' Log error message and exit program. '''
    logging.error(message_error(index, *args))
    logging.error(message_error(698))
    sys.exit(1)


def exit_silently():
    ''' Exit program. '''
    sys.exit(1)


def key_member_name(object):
    return object.get("name")

# -----------------------------------------------------------------------------
# do_* functions
#   Common function signature: do_XXX(args)
# -----------------------------------------------------------------------------


def do_awesome_groups(args):
    ''' Do a task. '''

    # Get context from CLI, environment variables, and ini files.

    config = get_configuration(args)

    # Prolog.

    logging.info(entry_template(config))

    # Validate input.

    validate_configuration(config)

    # Pull variables from config.

    github_access_token = config.get("github_access_token")
    organization = config.get("organization")

    # Log into GitHub.

    github = Github(github_access_token)

    # Iterate through all repositories.

    github_organization = github.get_organization(organization)
    for repo in github_organization.get_repos():

        # Get topics for the repository.

        topics = repo.get_topics()

        # Black-listed topics.

        if "deprecated" in topics:
            continue
        if "obsolete" in topics:
            continue
        if "archived" in topics:
            continue

        # Process only specified topics.

        for topic in topics:
            if topic in awesome_topics.keys():
                member = {
                    "name": repo.name,
                    "url": repo.html_url,
                    "description": repo.description
                }
                awesome_topics.get(topic, []).get("members", []).append(member)

    # Print groups.

    for topic_key, topic_value in awesome_topics.items():
        print("\n## {0}".format(topic_value.get("title", "Unknown")))
        print("\n*{0}*\n".format(topic_value.get("description", "Unknown")))

        # Print members in alphabetical order.

        members = sorted(topic_value.get("members", []), key=key_member_name)
        for member in members:
            print("1. [{0}]({1}) - {2}".format(member.get("name"), member.get("url"), member.get("description", "")))

    # Epilog.

    logging.info(exit_template(config))


def do_awesome_page(args):
    ''' Do a task. '''

    # Get context from CLI, environment variables, and ini files.

    config = get_configuration(args)

    # Validate input.

    validate_configuration(config)

    # Pull variables from config.

    github_access_token = config.get("github_access_token")
    organization = config.get("organization")

    # Log into GitHub.

    github = Github(github_access_token)

    # Iterate through all repositories.

    github_organization = github.get_organization(organization)
    for repo in github_organization.get_repos():

        # Get topics for the repository.

        topics = repo.get_topics()

        # Black-listed topics.

        if "archived" in topics:
            continue

        elif "deprecated" in topics:
            continue

        # Separate out "obsolete" repositories.

        elif "obsolete" in topics:
            member = {
                "name": repo.name,
                "url": repo.html_url,
                "description": repo.description
            }
            awesome_topics.get("obsolete", []).get("members", []).append(member)

        # Separate out "obsolete" repositories.

        elif "under-construction" in topics:
            member = {
                "name": repo.name,
                "url": repo.html_url,
                "description": repo.description
            }
            awesome_topics.get("under-construction", []).get("members", []).append(member)

        # After passing the "guards" (obsolete, deprecated, archived), process repository.

        else:

            # Process only specified topics.

            for topic in topics:
                if topic in awesome_topics.keys():
                    member = {
                        "name": repo.name,
                        "url": repo.html_url,
                        "description": repo.description
                    }
                    awesome_topics.get(topic, []).get("members", []).append(member)

    # Print prolog.

    for prolog_line in prolog_lines:
        print(prolog_line)

    # Print groups.

    for topic_key, topic_value in awesome_topics.items():
        print("\n## {0}".format(topic_value.get("title", "Unknown")))
        print("\n*{0}*\n".format(topic_value.get("description", "Unknown")))

        # Print members in alphabetical order.

        members = sorted(topic_value.get("members", []), key=key_member_name)
        for member in members:
            print("1. [{0}]({1}) - {2}".format(member.get("name"), member.get("url"), member.get("description", "")))

    # Print epilog.

    for epilog_line in epilog_lines:
        print(epilog_line)


def do_awesome_page_excluded(args):
    ''' Do a task. '''

    # Get context from CLI, environment variables, and ini files.

    config = get_configuration(args)

    # Validate input.

    validate_configuration(config)

    # Pull variables from config.

    github_access_token = config.get("github_access_token")
    organization = config.get("organization")

    # Log into GitHub.

    github = Github(github_access_token)

    # Iterate through all repositories.

    github_organization = github.get_organization(organization)
    for repo in github_organization.get_repos():

        # Get topics for the repository.

        topics = repo.get_topics()

        # Black-listed topics.

        if "archived" in topics:
            print("  Archived: {}".format(repo.name))
        elif "deprecated" in topics:
            print("Deprecated: {}".format(repo.name))
        elif len(topics) == 0:
            print("No  topics: {}".format(repo.name))
        else:
            found = False
            for topic in topics:
                if topic in awesome_topics.keys():
                    found = True
            if not found:
                print("Not  found: {}".format(repo.name))


def do_version(args):
    ''' Log version information. '''

    logging.info(message_info(294, __version__, __updated__))

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


if __name__ == "__main__":

    # Configure logging. See https://docs.python.org/2/library/logging.html#levels

    log_level_map = {
        "notset": logging.NOTSET,
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "fatal": logging.FATAL,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }

    log_level_parameter = os.getenv("GITHUB_LOG_LEVEL", "info").lower()
    log_level = log_level_map.get(log_level_parameter, logging.INFO)
    logging.basicConfig(format=log_format, level=log_level)

    # Trap signals temporarily until args are parsed.

    signal.signal(signal.SIGTERM, bootstrap_signal_handler)
    signal.signal(signal.SIGINT, bootstrap_signal_handler)

    # Parse the command line arguments.

    subcommand = os.getenv("GITHUB_SUBCOMMAND", None)
    parser = get_parser()
    if len(sys.argv) > 1:
        args = parser.parse_args()
        subcommand = args.subcommand
    elif subcommand:
        args = argparse.Namespace(subcommand=subcommand)
    else:
        parser.print_help()
        if len(os.getenv("GITHUB_DOCKER_LAUNCHED", "")):
            subcommand = "sleep"
            args = argparse.Namespace(subcommand=subcommand)
            do_sleep(args)
        exit_silently()

    # Catch interrupts. Tricky code: Uses currying.

    signal_handler = create_signal_handler_function(args)
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Transform subcommand from CLI parameter to function name string.

    subcommand_function_name = "do_{0}".format(subcommand.replace('-', '_'))

    # Test to see if function exists in the code.

    if subcommand_function_name not in globals():
        logging.warning(message_warning(596, subcommand))
        parser.print_help()
        exit_silently()

    # Tricky code for calling function based on string.

    globals()[subcommand_function_name](args)
