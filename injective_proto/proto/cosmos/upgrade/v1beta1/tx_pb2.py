from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/upgrade/v1beta1/tx.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective_proto.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from injective_proto.proto.cosmos.upgrade.v1beta1 import upgrade_pb2 as cosmos_dot_upgrade_dot_v1beta1_dot_upgrade__pb2
from injective_proto.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from injective_proto.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\x1f\x63osmos/upgrade/v1beta1/tx.proto\x12\x16\x63osmos.upgrade.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a$cosmos/upgrade/v1beta1/upgrade.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\"\xbb\x01\n\x12MsgSoftwareUpgrade\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12;\n\x04plan\x18\x02 \x01(\x0b\x32\x1c.cosmos.upgrade.v1beta1.PlanB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x04plan:0\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1d\x63osmos-sdk/MsgSoftwareUpgrade\"\x1c\n\x1aMsgSoftwareUpgradeResponse\"z\n\x10MsgCancelUpgrade\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority:.\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1b\x63osmos-sdk/MsgCancelUpgrade\"\x1a\n\x18MsgCancelUpgradeResponse2\xec\x01\n\x03Msg\x12q\n\x0fSoftwareUpgrade\x12*.cosmos.upgrade.v1beta1.MsgSoftwareUpgrade\x1a\x32.cosmos.upgrade.v1beta1.MsgSoftwareUpgradeResponse\x12k\n\rCancelUpgrade\x12(.cosmos.upgrade.v1beta1.MsgCancelUpgrade\x1a\x30.cosmos.upgrade.v1beta1.MsgCancelUpgradeResponse\x1a\x05\x80\xe7\xb0*\x01\x42\xbd\x01\n\x1a\x63om.cosmos.upgrade.v1beta1B\x07TxProtoP\x01Z\x1c\x63osmossdk.io/x/upgrade/types\xa2\x02\x03\x43UX\xaa\x02\x16\x43osmos.Upgrade.V1beta1\xca\x02\x16\x43osmos\\Upgrade\\V1beta1\xe2\x02\"Cosmos\\Upgrade\\V1beta1\\GPBMetadata\xea\x02\x18\x43osmos::Upgrade::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.upgrade.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.cosmos.upgrade.v1beta1B\007TxProtoP\001Z\034cosmossdk.io/x/upgrade/types\242\002\003CUX\252\002\026Cosmos.Upgrade.V1beta1\312\002\026Cosmos\\Upgrade\\V1beta1\342\002\"Cosmos\\Upgrade\\V1beta1\\GPBMetadata\352\002\030Cosmos::Upgrade::V1beta1'
  _globals['_MSGSOFTWAREUPGRADE'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGSOFTWAREUPGRADE'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSOFTWAREUPGRADE'].fields_by_name['plan']._loaded_options = None
  _globals['_MSGSOFTWAREUPGRADE'].fields_by_name['plan']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGSOFTWAREUPGRADE']._loaded_options = None
  _globals['_MSGSOFTWAREUPGRADE']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\035cosmos-sdk/MsgSoftwareUpgrade'
  _globals['_MSGCANCELUPGRADE'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGCANCELUPGRADE'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGCANCELUPGRADE']._loaded_options = None
  _globals['_MSGCANCELUPGRADE']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\033cosmos-sdk/MsgCancelUpgrade'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGSOFTWAREUPGRADE']._serialized_start=191
  _globals['_MSGSOFTWAREUPGRADE']._serialized_end=378
  _globals['_MSGSOFTWAREUPGRADERESPONSE']._serialized_start=380
  _globals['_MSGSOFTWAREUPGRADERESPONSE']._serialized_end=408
  _globals['_MSGCANCELUPGRADE']._serialized_start=410
  _globals['_MSGCANCELUPGRADE']._serialized_end=532
  _globals['_MSGCANCELUPGRADERESPONSE']._serialized_start=534
  _globals['_MSGCANCELUPGRADERESPONSE']._serialized_end=560
  _globals['_MSG']._serialized_start=563
  _globals['_MSG']._serialized_end=799
# @@protoc_insertion_point(module_scope)
