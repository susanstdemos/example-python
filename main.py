from jwt import algorithms
from django.utils import formats
from rsa import cli
from feedparser import feedparser
from requests import sessions
from lib.Crypto.PublicKey import ElGamal
from tlslite.tlsrecordlayer import TLSRecordLayer

if __name__ == '__main__':
    formats.get_format()
    algorithms.HMACAlgorithm.prepare_key()
    cli.VerifyOperation.perform_operation()
    sessions.SessionRedirectMixin.resolve_redirects()
    ElGamal.generate()
    feedparser._open_resource()
    tlsrecordlayer.TLSRecordLayer._decryptRecord()
    # yo_dawg_i_heard_you_liked_methods()

#
# def yo_dawg_i_heard_you_liked_methods():
#     so_we_put_a_method_in_your_method()
#
# def so_we_put_a_method_in_your_method():
