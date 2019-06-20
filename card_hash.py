# coding: utf-8

import hashlib
import binascii
import nfc

def startup(targets):
    print("waiting for new NFC tags...")
    return targets

def connected(tag):
    print("connected:")
    print(tag)

    try:
        # 製造ID (IDm)
        idm = binascii.hexlify(tag.identifier).upper()
        print('IDm: %s' % idm)

        # 製造パラメータ (PMm)
        pmm = binascii.hexlify(tag.pmm).upper()
        print('PMm: %s' % pmm)

        # システムコード
        syscode = "%04X" % tag.sys
        print('sys: %s' % syscode)

        # ハッシュ値の生成
        hexdigest = sha512(idm, pmm, syscode)
        print('sha512(IDm, PMm, sys): %s' % hexdigest)
        return True
    except:
        return False

def sha512(*args):
    return hashlib.sha512(''.join(args)).hexdigest()

if __name__ == '__main__':

    clf = nfc.ContactlessFrontend('usb')
    print(clf)
    if clf:
        while clf.connect(rdwr={
                'on-startup': startup,
                'on-connect': connected, }):
            pass
