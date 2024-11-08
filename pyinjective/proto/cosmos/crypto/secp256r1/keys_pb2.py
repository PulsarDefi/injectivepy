from pyinjective.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crypto/secp256r1/keys.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\"cosmos/crypto/secp256r1/keys.proto\x12\x17\x63osmos.crypto.secp256r1\x1a\x14gogoproto/gogo.proto\"\'\n\x06PubKey\x12\x1d\n\x03key\x18\x01 \x01(\x0c\x42\x0b\xda\xde\x1f\x07\x65\x63\x64saPKR\x03key\".\n\x07PrivKey\x12#\n\x06secret\x18\x01 \x01(\x0c\x42\x0b\xda\xde\x1f\x07\x65\x63\x64saSKR\x06secretB\xe6\x01\n\x1b\x63om.cosmos.crypto.secp256r1B\tKeysProtoP\x01Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256r1\xa2\x02\x03\x43\x43S\xaa\x02\x17\x43osmos.Crypto.Secp256r1\xca\x02\x17\x43osmos\\Crypto\\Secp256r1\xe2\x02#Cosmos\\Crypto\\Secp256r1\\GPBMetadata\xea\x02\x19\x43osmos::Crypto::Secp256r1\xc8\xe1\x1e\x00\xd8\xe1\x1e\x00\xc8\xe3\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crypto.secp256r1.keys_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.cosmos.crypto.secp256r1B\tKeysProtoP\001Z2github.com/cosmos/cosmos-sdk/crypto/keys/secp256r1\242\002\003CCS\252\002\027Cosmos.Crypto.Secp256r1\312\002\027Cosmos\\Crypto\\Secp256r1\342\002#Cosmos\\Crypto\\Secp256r1\\GPBMetadata\352\002\031Cosmos::Crypto::Secp256r1\310\341\036\000\330\341\036\000\310\343\036\001'
  _globals['_PUBKEY'].fields_by_name['key']._loaded_options = None
  _globals['_PUBKEY'].fields_by_name['key']._serialized_options = b'\332\336\037\007ecdsaPK'
  _globals['_PRIVKEY'].fields_by_name['secret']._loaded_options = None
  _globals['_PRIVKEY'].fields_by_name['secret']._serialized_options = b'\332\336\037\007ecdsaSK'
  _globals['_PUBKEY']._serialized_start=85
  _globals['_PUBKEY']._serialized_end=124
  _globals['_PRIVKEY']._serialized_start=126
  _globals['_PRIVKEY']._serialized_end=172
# @@protoc_insertion_point(module_scope)
