#####################################################
# COMP0061 -- Privacy Enhancing Technologies -- Lab 01
#
# Basics of Petlib, encryption, signatures and
# an end-to-end encryption system.
#
# Run the tests through:
# $ pytest -v


#####################################################
# TASK 1 -- Ensure petlib and pytest are installed on
#           the System. Ensure lab code can be
#           imported

import petlib

#####################################################
# TASK 2 -- Symmetric encryption using AES-GCM 
#           (Galois Counter Mode)
#
# Implement encryption and decryption functions
# that simply performs AES_GCM symmetric encryption
# and decryption using the functions in petlib.cipher.

from os import urandom

import pytest
from petlib.cipher import Cipher
from pytest import raises


def encrypt_message(key, message):
    """ Encrypt a message under a key given as input """

    # TODO: ADD YOUR CODE HERE

    return iv, ciphertext, tag


def decrypt_message(key, iv, ciphertext, tag):
    """ Decrypt a cipher text under a key given as input

        In case the decryption fails, throw an exception.
    """
    # TODO: ADD YOUR CODE HERE

    return plain


#####################################################
# TASK 3 -- Understand Elliptic Curve Arithmetic
#           - Test if a point is on a curve.
#           - Implement Point addition.
#           - Implement Point doubling.
#           - Implement Scalar multiplication (double & add).
#           - Implement Scalar multiplication (Montgomery ladder).
#
# MUST NOT USE ANY OF THE petlib.ec FUNCTIONS. Only petlib.bn!

from petlib.bn import Bn


def is_point_on_curve(a, b, p, x, y):
    """
    Check that a point (x, y) is on the curve defined by a,b and prime p.
    Reminder: an Elliptic Curve on a prime field p is defined as:

              y^2 = x^3 + ax + b (mod p)
                  (Weierstrass form)

    Return True if point (x,y) is on curve, otherwise False.
    By convention a (None, None) point represents "infinity".
    """
    assert isinstance(a, Bn)
    assert isinstance(b, Bn)
    assert isinstance(p, Bn) and p > 0
    assert (isinstance(x, Bn) and isinstance(y, Bn)) \
           or (x is None and y is None)

    if x is None and y is None:
        return True

    lhs = (y * y) % p
    rhs = (x * x * x + a * x + b) % p
    on_curve = (lhs == rhs)

    return on_curve


def point_add(a, b, p, x0, y0, x1, y1):
    """Define the "addition" operation for 2 EC Points.

    Reminder: (xr, yr) = (xq, yq) + (xp, yp)
    is defined as:
        lam = (yq - yp) * (xq - xp)^-1 (mod p)
        xr  = lam^2 - xp - xq (mod p)
        yr  = lam * (xp - xr) - yp (mod p)

    Return the point resulting from the addition by
    implementing the above pseudocode.
    Raises an Exception if the points are equal.
    Make sure you can handle the case where one point is the negation
    of the other: (xq, yq) == -(xp, yp) == (xp, -yp).
    """

    # TODO: ADD YOUR CODE BELOW
    xr, yr = None, None

    return xr, yr


def point_double(a, b, p, x, y):
    """Define "doubling" an EC point.
     A special case, when a point needs to be added to itself.

     Reminder:
        lam = (3 * xp ^ 2 + a) * (2 * yp) ^ -1 (mod p)
        xr  = lam ^ 2 - 2 * xp
        yr  = lam * (xp - xr) - yp (mod p)

    Returns the point representing the double of the input (x, y).
    """

    # ADD YOUR CODE BELOW
    xr, yr = None, None

    return xr, yr


def point_scalar_multiplication_double_and_add(a, b, p, x, y, scalar):
    """
    Implement Point multiplication with a scalar:
        r * (x, y) = (x, y) + ... + (x, y)    (r times)

    Reminder of Double and Multiply algorithm: r * P
        Q = infinity
        for i = 0 to num_bits(r)-1
            if bit i of r == 1 then
                Q = Q + P
            P = 2 * P
        return Q

    """
    Q = (None, None)
    P = (x, y)

    for i in range(scalar.num_bits()):
        # TODO: ADD YOUR CODE HERE
        pass

    return Q


def point_scalar_multiplication_montgomerry_ladder(a, b, p, x, y, scalar):
    """
    Implement Point multiplication with a scalar:
        r * (x, y) = (x, y) + ... + (x, y)    (r times)

    Reminder of Double and Multiply algorithm: r * P
        R0 = infinity
        R1 = P
        for i in num_bits(P)-1 to zero:
            if di = 0:
                R1 = R0 + R1
                R0 = 2R0
            else
                R0 = R0 + R1
                R1 = 2 R1
        return R0

    """
    R0 = (None, None)
    R1 = (x, y)

    for i in reversed(range(0, scalar.num_bits())):
        # TODO: ADD YOUR CODE HERE
        pass

    return R0


#####################################################
# TASK 4 -- Standard ECDSA signatures
#
#          - Implement a key / param generation 
#          - Implement ECDSA signature using petlib.ecdsa
#          - Implement ECDSA signature verification 
#            using petlib.ecdsa

from hashlib import sha256
from petlib.ec import EcGroup
from petlib.ecdsa import do_ecdsa_sign, do_ecdsa_verify


def ecdsa_key_gen(group=None):
    """ Returns an EC group, a random private key for signing 
        and the corresponding public key for verification"""
    if group is None:
        group = EcGroup()
    priv_sign = group.order().random()
    pub_verify = priv_sign * group.generator()
    return group, priv_sign, pub_verify


def ecdsa_sign(group, priv_sign, message):
    """ Sign the SHA256 digest of the message using ECDSA and return a signature """

    # TODO: ADD YOUR CODE HERE

    return sig


def ecdsa_verify(group, pub_verify, message, sig):
    """ Verify the ECDSA signature on the message """

    # TODO: ADD YOUR CODE HERE

    return res


#####################################################
# TASK 5 -- Diffie-Hellman Key Exchange and Derivation
#           - use Bob's public key to derive a shared key.
#           - Use Bob's public key to encrypt a message.
#           - Use Bob's private key to decrypt the message.

def dh_get_key(group=None):
    """ Generate a DH key pair """
    if group is None:
        group = EcGroup()
    priv_dec = group.order().random()
    pub_enc = priv_dec * group.generator()
    return group, priv_dec, pub_enc


def dh_encrypt(pub, message, alice_sig):
    """ Assume you know the public key of someone else (Bob), 
    and wish to Encrypt a message for them.
        - Generate a fresh DH key for this message.
        - Derive a fresh shared key.
        - Use the shared key to generate a symmetric key
        - Use the symmetric key to AES_GCM encrypt the message.
        - Sign the message with Alice's signing key.
    """

    # TODO: ADD YOUR CODE HERE
    pass


def dh_decrypt(priv, ciphertext, alice_ver):
    """ Decrypt a received message encrypted using your public key, 
    of which the private key is provided.
    Verify the message came from Alice using her verification
    key."""

    # TODO: ADD YOUR CODE HERE
    pass


# TODO: POPULATE THESE (OR MORE) TESTS
# Pytest assumes any function that starts with `test_` is a test.
# To create additional tests, add more functions below the given stubs
# and mark them as being part of task5.
# Ensure they run using the "pytest lab01.py" command.

@pytest.mark.task5
def test_encrypt():
    group, _, bob_pub_enc = dh_get_key()
    _, alice_sign, _, = ecdsa_key_gen(group)
    assert False


@pytest.mark.task5
def test_decrypt():
    group, bob_priv_enc, bob_pub_enc = dh_get_key()
    _, alice_sign, alice_ver, = ecdsa_key_gen(group)
    assert False


@pytest.mark.task5
def test_fails():
    assert False


"""
Run the tests with test coverage:
$ pytest --cov-report html --cov lab01

What is your test coverage? Where is it missing cases?

TODO: ADD YOUR ANSWER HERE
"""


#####################################################
# TASK 6 -- Time EC scalar multiplication
#             Open Task.
#           
#           - Time your implementations of scalar multiplication
#             (use time.perf_counter_ns() for measurements) for
#             different scalar sizes
#           - Print reports on timing dependencies on secrets.
#           - Fix one implementation to not leak information.

def time_scalar_mul():  # pragma: no cover
    # TODO: ADD YOUR CODE HERE
    pass
