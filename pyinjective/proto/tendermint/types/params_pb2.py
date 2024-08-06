# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/types/params.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dtendermint/types/params.proto\x12\x10tendermint.types\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\"\xb2\x02\n\x0f\x43onsensusParams\x12\x33\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x1d.tendermint.types.BlockParamsR\x05\x62lock\x12<\n\x08\x65vidence\x18\x02 \x01(\x0b\x32 .tendermint.types.EvidenceParamsR\x08\x65vidence\x12?\n\tvalidator\x18\x03 \x01(\x0b\x32!.tendermint.types.ValidatorParamsR\tvalidator\x12\x39\n\x07version\x18\x04 \x01(\x0b\x32\x1f.tendermint.types.VersionParamsR\x07version\x12\x30\n\x04\x61\x62\x63i\x18\x05 \x01(\x0b\x32\x1c.tendermint.types.ABCIParamsR\x04\x61\x62\x63i\"I\n\x0b\x42lockParams\x12\x1b\n\tmax_bytes\x18\x01 \x01(\x03R\x08maxBytes\x12\x17\n\x07max_gas\x18\x02 \x01(\x03R\x06maxGasJ\x04\x08\x03\x10\x04\"\xa9\x01\n\x0e\x45videnceParams\x12+\n\x12max_age_num_blocks\x18\x01 \x01(\x03R\x0fmaxAgeNumBlocks\x12M\n\x10max_age_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01R\x0emaxAgeDuration\x12\x1b\n\tmax_bytes\x18\x03 \x01(\x03R\x08maxBytes\"?\n\x0fValidatorParams\x12\"\n\rpub_key_types\x18\x01 \x03(\tR\x0bpubKeyTypes:\x08\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01\"+\n\rVersionParams\x12\x10\n\x03\x61pp\x18\x01 \x01(\x04R\x03\x61pp:\x08\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01\"Z\n\x0cHashedParams\x12&\n\x0f\x62lock_max_bytes\x18\x01 \x01(\x03R\rblockMaxBytes\x12\"\n\rblock_max_gas\x18\x02 \x01(\x03R\x0b\x62lockMaxGas\"O\n\nABCIParams\x12\x41\n\x1dvote_extensions_enable_height\x18\x01 \x01(\x03R\x1avoteExtensionsEnableHeightB\xbd\x01\n\x14\x63om.tendermint.typesB\x0bParamsProtoP\x01Z3github.com/cometbft/cometbft/proto/tendermint/types\xa2\x02\x03TTX\xaa\x02\x10Tendermint.Types\xca\x02\x10Tendermint\\Types\xe2\x02\x1cTendermint\\Types\\GPBMetadata\xea\x02\x11Tendermint::Types\xa8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.types.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.tendermint.typesB\013ParamsProtoP\001Z3github.com/cometbft/cometbft/proto/tendermint/types\242\002\003TTX\252\002\020Tendermint.Types\312\002\020Tendermint\\Types\342\002\034Tendermint\\Types\\GPBMetadata\352\002\021Tendermint::Types\250\342\036\001'
  _globals['_EVIDENCEPARAMS'].fields_by_name['max_age_duration']._loaded_options = None
  _globals['_EVIDENCEPARAMS'].fields_by_name['max_age_duration']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _globals['_VALIDATORPARAMS']._loaded_options = None
  _globals['_VALIDATORPARAMS']._serialized_options = b'\270\240\037\001\350\240\037\001'
  _globals['_VERSIONPARAMS']._loaded_options = None
  _globals['_VERSIONPARAMS']._serialized_options = b'\270\240\037\001\350\240\037\001'
  _globals['_CONSENSUSPARAMS']._serialized_start=106
  _globals['_CONSENSUSPARAMS']._serialized_end=412
  _globals['_BLOCKPARAMS']._serialized_start=414
  _globals['_BLOCKPARAMS']._serialized_end=487
  _globals['_EVIDENCEPARAMS']._serialized_start=490
  _globals['_EVIDENCEPARAMS']._serialized_end=659
  _globals['_VALIDATORPARAMS']._serialized_start=661
  _globals['_VALIDATORPARAMS']._serialized_end=724
  _globals['_VERSIONPARAMS']._serialized_start=726
  _globals['_VERSIONPARAMS']._serialized_end=769
  _globals['_HASHEDPARAMS']._serialized_start=771
  _globals['_HASHEDPARAMS']._serialized_end=861
  _globals['_ABCIPARAMS']._serialized_start=863
  _globals['_ABCIPARAMS']._serialized_end=942
# @@protoc_insertion_point(module_scope)
