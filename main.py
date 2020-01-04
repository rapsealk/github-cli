#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys
import requests


GitHubUserOAuthToken = "PUT_OAUTH_TOKEN_HERE"


class GitHubRepositoryInfo:
    """
    Documentation https://developer.github.com/v3/repos/#parameters-4
    ---
    Args:
        name (str): Required. The name of the repository.
        description (str): A short description of the repository. (optional)
        homepage (str): A URL with more information about the repository. (optional)
        private (bool): Either true to create a private repository or false to create a public one.
                        Creating private repositories requires a paid GitHub account.
                        Default: false
        has_issues (bool): Either true to enable issues for this repository or false to disable them.
                           Default: true.
        has_projects (bool): Either true to enable projects for this repository or false to disable them.
                             Default: true.
                             Note: If you're creating a repository in an organization that has disabled repository projects,
                                   the default is false, and if you pass true, the API returns an error.
        has_wiki (bool): Either true to enable the wiki for this repository or false to disable it. 
                         Default: true.
    """
    def __init__(self, **kwargs):
        obj = {
            "name": "",
            "description": "",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }
        for key in kwargs:
            try:
                obj[key] = kwargs[key]
            except KeyError:
                continue
            except Exception as e:
                sys.stderr.write('Error: %s\n' % e)

        self.name = obj["name"]
        self.description = obj["description"]
        self.homepage = obj["homepage"]
        self.private = obj["private"]
        self.has_issues = obj["has_issues"]
        self.has_projects = obj["has_projects"]
        self.has_wiki = obj["has_wiki"]

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "homepage": self.homepage,
            "private": self.private,
            "has_issues": self.has_issues,
            "has_projects": self.has_projects,
            "has_wiki": self.has_wiki
        }

    def __str__(self):
        return self.__class__.__name__ + str(self.to_dict())


class GitHubClient:

    BASE_URL = "https://api.github.com"
    _PATH_AUTHORIZATIONS = "/authorizations"
    _PATH_REPOSITORY = "/user/repos"

    def __init__(self):
        pass

    def get_authorizations(self):
        url = GitHubClient.BASE_URL + GitHubClient._PATH_AUTHORIZATIONS
        try:
            response = requests.get(url)
            print(response.status_code)
        except Exception as e:
            sys.stderr.write('Error: %s\n' % e)

    def create_repository(self, info: GitHubRepositoryInfo):
        url = GitHubClient.BASE_URL + GitHubClient._PATH_REPOSITORY
        headers = {
            'Content-Type': 'application/json; charset=utf-8;',
            'Authorization': 'token %s' % GitHubUserOAuthToken
        }
        try:
            response = requests.post(url, headers=headers, data=info.to_dict())
            return response.status_code
        except Exception as e:
            sys.stderr.write('Error: %s\n' % e)
        return -1


if __name__ == "__main__":
    client = GitHubClient()
