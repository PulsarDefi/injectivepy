from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/base/tendermint/v1beta1/types.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective_proto.proto.tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from injective_proto.proto.tendermint.types import evidence_pb2 as tendermint_dot_types_dot_evidence__pb2
from injective_proto.proto.tendermint.version import types_pb2 as tendermint_dot_version_dot_types__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from injective_proto.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n*cosmos/base/tendermint/v1beta1/types.proto\x12\x1e\x63osmos.base.tendermint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ctendermint/types/types.proto\x1a\x1ftendermint/types/evidence.proto\x1a\x1etendermint/version/types.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x11\x61mino/amino.proto\"\x8b\x02\n\x05\x42lock\x12I\n\x06header\x18\x01 \x01(\x0b\x32&.cosmos.base.tendermint.v1beta1.HeaderB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06header\x12\x35\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x16.tendermint.types.DataB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x04\x64\x61ta\x12\x45\n\x08\x65vidence\x18\x03 \x01(\x0b\x32\x1e.tendermint.types.EvidenceListB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x08\x65vidence\x12\x39\n\x0blast_commit\x18\x04 \x01(\x0b\x32\x18.tendermint.types.CommitR\nlastCommit\"\xf5\x04\n\x06Header\x12\x42\n\x07version\x18\x01 \x01(\x0b\x32\x1d.tendermint.version.ConsensusB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x07version\x12&\n\x08\x63hain_id\x18\x02 \x01(\tB\x0b\xe2\xde\x1f\x07\x43hainIDR\x07\x63hainId\x12\x16\n\x06height\x18\x03 \x01(\x03R\x06height\x12=\n\x04time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01R\x04time\x12H\n\rlast_block_id\x18\x05 \x01(\x0b\x32\x19.tendermint.types.BlockIDB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x0blastBlockId\x12(\n\x10last_commit_hash\x18\x06 \x01(\x0cR\x0elastCommitHash\x12\x1b\n\tdata_hash\x18\x07 \x01(\x0cR\x08\x64\x61taHash\x12\'\n\x0fvalidators_hash\x18\x08 \x01(\x0cR\x0evalidatorsHash\x12\x30\n\x14next_validators_hash\x18\t \x01(\x0cR\x12nextValidatorsHash\x12%\n\x0e\x63onsensus_hash\x18\n \x01(\x0cR\rconsensusHash\x12\x19\n\x08\x61pp_hash\x18\x0b \x01(\x0cR\x07\x61ppHash\x12*\n\x11last_results_hash\x18\x0c \x01(\x0cR\x0flastResultsHash\x12#\n\revidence_hash\x18\r \x01(\x0cR\x0c\x65videnceHash\x12)\n\x10proposer_address\x18\x0e \x01(\tR\x0fproposerAddressB\x80\x02\n\"com.cosmos.base.tendermint.v1beta1B\nTypesProtoP\x01Z3github.com/cosmos/cosmos-sdk/client/grpc/cmtservice\xa2\x02\x03\x43\x42T\xaa\x02\x1e\x43osmos.Base.Tendermint.V1beta1\xca\x02\x1e\x43osmos\\Base\\Tendermint\\V1beta1\xe2\x02*Cosmos\\Base\\Tendermint\\V1beta1\\GPBMetadata\xea\x02!Cosmos::Base::Tendermint::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.tendermint.v1beta1.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.cosmos.base.tendermint.v1beta1B\nTypesProtoP\001Z3github.com/cosmos/cosmos-sdk/client/grpc/cmtservice\242\002\003CBT\252\002\036Cosmos.Base.Tendermint.V1beta1\312\002\036Cosmos\\Base\\Tendermint\\V1beta1\342\002*Cosmos\\Base\\Tendermint\\V1beta1\\GPBMetadata\352\002!Cosmos::Base::Tendermint::V1beta1'
  _globals['_BLOCK'].fields_by_name['header']._loaded_options = None
  _globals['_BLOCK'].fields_by_name['header']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_BLOCK'].fields_by_name['data']._loaded_options = None
  _globals['_BLOCK'].fields_by_name['data']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_BLOCK'].fields_by_name['evidence']._loaded_options = None
  _globals['_BLOCK'].fields_by_name['evidence']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_HEADER'].fields_by_name['version']._loaded_options = None
  _globals['_HEADER'].fields_by_name['version']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_HEADER'].fields_by_name['chain_id']._loaded_options = None
  _globals['_HEADER'].fields_by_name['chain_id']._serialized_options = b'\342\336\037\007ChainID'
  _globals['_HEADER'].fields_by_name['time']._loaded_options = None
  _globals['_HEADER'].fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001\250\347\260*\001'
  _globals['_HEADER'].fields_by_name['last_block_id']._loaded_options = None
  _globals['_HEADER'].fields_by_name['last_block_id']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_BLOCK']._serialized_start=248
  _globals['_BLOCK']._serialized_end=515
  _globals['_HEADER']._serialized_start=518
  _globals['_HEADER']._serialized_end=1147
# @@protoc_insertion_point(module_scope)
