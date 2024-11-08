from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/batch.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.injective.peggy.v1 import attestation_pb2 as injective_dot_peggy_dot_v1_dot_attestation__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\x1einjective/peggy/v1/batch.proto\x12\x12injective.peggy.v1\x1a$injective/peggy/v1/attestation.proto\"\xe0\x01\n\x0fOutgoingTxBatch\x12\x1f\n\x0b\x62\x61tch_nonce\x18\x01 \x01(\x04R\nbatchNonce\x12#\n\rbatch_timeout\x18\x02 \x01(\x04R\x0c\x62\x61tchTimeout\x12J\n\x0ctransactions\x18\x03 \x03(\x0b\x32&.injective.peggy.v1.OutgoingTransferTxR\x0ctransactions\x12%\n\x0etoken_contract\x18\x04 \x01(\tR\rtokenContract\x12\x14\n\x05\x62lock\x18\x05 \x01(\x04R\x05\x62lock\"\xdd\x01\n\x12OutgoingTransferTx\x12\x0e\n\x02id\x18\x01 \x01(\x04R\x02id\x12\x16\n\x06sender\x18\x02 \x01(\tR\x06sender\x12!\n\x0c\x64\x65st_address\x18\x03 \x01(\tR\x0b\x64\x65stAddress\x12?\n\x0b\x65rc20_token\x18\x04 \x01(\x0b\x32\x1e.injective.peggy.v1.ERC20TokenR\nerc20Token\x12;\n\terc20_fee\x18\x05 \x01(\x0b\x32\x1e.injective.peggy.v1.ERC20TokenR\x08\x65rc20FeeB\xdb\x01\n\x16\x63om.injective.peggy.v1B\nBatchProtoP\x01ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types\xa2\x02\x03IPX\xaa\x02\x12Injective.Peggy.V1\xca\x02\x12Injective\\Peggy\\V1\xe2\x02\x1eInjective\\Peggy\\V1\\GPBMetadata\xea\x02\x14Injective::Peggy::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.peggy.v1.batch_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.injective.peggy.v1B\nBatchProtoP\001ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types\242\002\003IPX\252\002\022Injective.Peggy.V1\312\002\022Injective\\Peggy\\V1\342\002\036Injective\\Peggy\\V1\\GPBMetadata\352\002\024Injective::Peggy::V1'
  _globals['_OUTGOINGTXBATCH']._serialized_start=93
  _globals['_OUTGOINGTXBATCH']._serialized_end=317
  _globals['_OUTGOINGTRANSFERTX']._serialized_start=320
  _globals['_OUTGOINGTRANSFERTX']._serialized_end=541
# @@protoc_insertion_point(module_scope)
