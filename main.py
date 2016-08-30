from jwt import algorithms
from django.utils import formats
from rsa import cli
from requests import sessions
import pyconsts
from Crypto.PublicKey import ElGamal

if __name__ == '__main__':
    formats.get_format()
    algorithms.HMACAlgorithm.prepare_key()
    cli.VerifyOperation.perform_operation()
    sessions.SessionRedirectMixin.resolve_redirects()
    pyconsts.index()
    ElGamal.generate(1, lambda x: 1)
