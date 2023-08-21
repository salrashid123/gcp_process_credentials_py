from datetime import datetime
import json
import subprocess
from subprocess import check_output
from datetime import datetime
import datetime

from google.auth import credentials
from google.auth import exceptions

_TIMEOUT = 2


class ProcessCredentials(credentials.CredentialsWithQuotaProject):

    def __init__(
        self,
        command,
        env=None,
        args=None,
        parser=None,
    ):

        super(ProcessCredentials, self).__init__()
        self._command = command
        self._args = args
        self._env = env
        self._parser = parser

        self.token = None
        self.expiry = datetime.datetime.utcnow()

    def refresh(self, request):
        self._update_token(request)

    def _update_token(self, request):

        args = self._command + self._args

        try:

            output = check_output(args=args, env=self._env,
                                  stderr=subprocess.PIPE, timeout=_TIMEOUT)

            if self._parser != None:
                output = self._parser(output)
            y = json.loads(output)
            self.token = y['access_token']
            #self.expiry = datetime.datetime.utcnow() + datetime.timedelta(seconds=y['expires_in'])
            self.expiry = datetime.datetime.now() + datetime.timedelta(seconds=y['expires_in'])

        except subprocess.CalledProcessError as e:
            raise exceptions.RefreshError(
                "Error running process: {}".format(e))
        except json.JSONDecodeError:
            raise exceptions.RefreshError(
                "Error getting loading response from  process: {}".format(output))
        except KeyError:
            raise exceptions.RefreshError(
                "Error getting finding token or expiry in response from  process: {}".format(output))
        except Exception as e:
            raise exceptions.RefreshError("Error : {}".format(e))

    def with_quota_project(self, quota_project_id):
        return self.__class__(
            self._command,
            self._args,
            self._env,
            self._parser,
            quota_project_id=quota_project_id,
        )
