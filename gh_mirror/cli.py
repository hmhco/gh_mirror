#!/usr/bin/python
# -*- coding: utf-8; -*-
#   Copyright [2013] [Robert Allen]
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import requests
import os
import logging
import subprocess


def fetch_repos(org, token, cwd="./"):
    """
    Collects all repos and iterates to update of clone as required
    :param org str:
    :param token str:
    :param cwd str:
    """
    uri = "https://api.github.com/orgs/{0}/repos".format(org)
    headers = {}
    if token is not None:
        headers["Authorization"] = "token {0}".format(token)
    i = 0
    try:
        r = requests.get(uri, headers=headers)
        if r.status_code != 200:
            raise requests.HTTPError("unsuccessful request made to %s" % uri)
        result = r.json()
        for repo in result:
            i += 1
            if os.path.exists('%s/%s' % (cwd, repo['name'])):
                git_update_mirror(repo=repo, cwd=cwd)
            else:
                git_clone_project(repo=repo, cwd=cwd)
    except OSError as error:
        logging.exception(error)
    return i


def git_update_mirror(repo, cwd):
    """
    Updates the project based on the information from the repo dict
    :param repo dict:
    :param cwd str:
    """
    args = ["git", "remote", "update", "-q"]
    path = "%s/%s" % (cwd, repo['name'])
    logging.info("updating %s" % (repo['full_name']))
    subprocess.Popen(args, cwd=path)


def git_clone_project(repo, cwd):
    """
    Clones a new project based on the repo dic
    :param repo dict:
    :param cwd str:
    """
    args = ["git", "clone", "-q", "--mirror", repo['ssh_url'], repo['name']]
    path = "%s" % cwd
    logging.info("cloning %s to %s" % (repo['ssh_url'], repo['name']))
    subprocess.Popen(args, cwd=path)


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser('GitHub Organization Repository Mirroring Tool')
    parser.add_argument('--loglevel', type=str, choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'],
                        help='Available levels are CRITICAL, ERROR, WARNING, INFO, DEBUG',
                        default="INFO")
    parser.add_argument('-d', '--directory', type=str, default=os.environ['HOME'],
                        help='The directory/path to mirror the repositories into, defaults to the user home.')
    parser.add_argument('-t', '--token', type=str, required=True,
                        help='The github oauth token authorized to pull from the repositories.')
    parser.add_argument('-o', '--organisation', type=str, required=True,
                        help='The Organisation name that owns the projects to mirror')
    options = parser.parse_args()

    log_level = getattr(logging, options.loglevel)
    logging.basicConfig(level=log_level, format='%(message)s')
    logging.info('Starting up...')
    count = fetch_repos(org=options.organisation, token=options.token, cwd=options.directory)
    logging.info("Run Complete [%s] repositories found..." % count)


if __name__ == "__main__":
    main()
