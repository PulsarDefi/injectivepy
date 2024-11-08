from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/evidence/v1beta1/tx.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from injective_proto.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from injective_proto.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from injective_proto.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n cosmos/evidence/v1beta1/tx.proto\x12\x17\x63osmos.evidence.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\"\xdc\x01\n\x11MsgSubmitEvidence\x12\x36\n\tsubmitter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tsubmitter\x12V\n\x08\x65vidence\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB$\xca\xb4- cosmos.evidence.v1beta1.EvidenceR\x08\x65vidence:7\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\tsubmitter\x8a\xe7\xb0*\x1c\x63osmos-sdk/MsgSubmitEvidence\"/\n\x19MsgSubmitEvidenceResponse\x12\x12\n\x04hash\x18\x04 \x01(\x0cR\x04hash2~\n\x03Msg\x12p\n\x0eSubmitEvidence\x12*.cosmos.evidence.v1beta1.MsgSubmitEvidence\x1a\x32.cosmos.evidence.v1beta1.MsgSubmitEvidenceResponse\x1a\x05\x80\xe7\xb0*\x01\x42\xc7\x01\n\x1b\x63om.cosmos.evidence.v1beta1B\x07TxProtoP\x01Z\x1d\x63osmossdk.io/x/evidence/types\xa2\x02\x03\x43\x45X\xaa\x02\x17\x43osmos.Evidence.V1beta1\xca\x02\x17\x43osmos\\Evidence\\V1beta1\xe2\x02#Cosmos\\Evidence\\V1beta1\\GPBMetadata\xea\x02\x19\x43osmos::Evidence::V1beta1\xa8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.evidence.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.cosmos.evidence.v1beta1B\007TxProtoP\001Z\035cosmossdk.io/x/evidence/types\242\002\003CEX\252\002\027Cosmos.Evidence.V1beta1\312\002\027Cosmos\\Evidence\\V1beta1\342\002#Cosmos\\Evidence\\V1beta1\\GPBMetadata\352\002\031Cosmos::Evidence::V1beta1\250\342\036\001'
  _globals['_MSGSUBMITEVIDENCE'].fields_by_name['submitter']._loaded_options = None
  _globals['_MSGSUBMITEVIDENCE'].fields_by_name['submitter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSUBMITEVIDENCE'].fields_by_name['evidence']._loaded_options = None
  _globals['_MSGSUBMITEVIDENCE'].fields_by_name['evidence']._serialized_options = b'\312\264- cosmos.evidence.v1beta1.Evidence'
  _globals['_MSGSUBMITEVIDENCE']._loaded_options = None
  _globals['_MSGSUBMITEVIDENCE']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\tsubmitter\212\347\260*\034cosmos-sdk/MsgSubmitEvidence'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGSUBMITEVIDENCE']._serialized_start=182
  _globals['_MSGSUBMITEVIDENCE']._serialized_end=402
  _globals['_MSGSUBMITEVIDENCERESPONSE']._serialized_start=404
  _globals['_MSGSUBMITEVIDENCERESPONSE']._serialized_end=451
  _globals['_MSG']._serialized_start=453
  _globals['_MSG']._serialized_end=579
# @@protoc_insertion_point(module_scope)
