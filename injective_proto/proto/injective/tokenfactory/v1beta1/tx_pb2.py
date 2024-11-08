from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/tokenfactory/v1beta1/tx.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective_proto.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from injective_proto.proto.cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from injective_proto.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from injective_proto.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from injective_proto.proto.injective.tokenfactory.v1beta1 import params_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_params__pb2
from injective_proto.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\'injective/tokenfactory/v1beta1/tx.proto\x12\x1einjective.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a+injective/tokenfactory/v1beta1/params.proto\x1a\x11\x61mino/amino.proto\"\xa2\x02\n\x0eMsgCreateDenom\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12/\n\x08subdenom\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:\"subdenom\"R\x08subdenom\x12#\n\x04name\x18\x03 \x01(\tB\x0f\xf2\xde\x1f\x0byaml:\"name\"R\x04name\x12)\n\x06symbol\x18\x04 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"symbol\"R\x06symbol\x12/\n\x08\x64\x65\x63imals\x18\x05 \x01(\rB\x13\xf2\xde\x1f\x0fyaml:\"decimals\"R\x08\x64\x65\x63imals:3\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*#injective/tokenfactory/create-denom\"\\\n\x16MsgCreateDenomResponse\x12\x42\n\x0fnew_token_denom\x18\x01 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:\"new_token_denom\"R\rnewTokenDenom\"\xab\x01\n\x07MsgMint\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12H\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:\"amount\"R\x06\x61mount:+\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1binjective/tokenfactory/mint\"\x11\n\x0fMsgMintResponse\"\xab\x01\n\x07MsgBurn\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12H\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:\"amount\"R\x06\x61mount:+\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1binjective/tokenfactory/burn\"\x11\n\x0fMsgBurnResponse\"\xcb\x01\n\x0eMsgChangeAdmin\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12&\n\x05\x64\x65nom\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"denom\"R\x05\x64\x65nom\x12\x31\n\tnew_admin\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"new_admin\"R\x08newAdmin:3\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*#injective/tokenfactory/change-admin\"\x18\n\x16MsgChangeAdminResponse\"\xcf\x01\n\x13MsgSetDenomMetadata\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12R\n\x08metadata\x18\x02 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x17\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"metadata\"R\x08metadata:9\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*)injective/tokenfactory/set-denom-metadata\"\x1d\n\x1bMsgSetDenomMetadataResponse\"\xc8\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x44\n\x06params\x18\x02 \x01(\x0b\x32&.injective.tokenfactory.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params:7\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*$injective/tokenfactory/update-params\"\x19\n\x17MsgUpdateParamsResponse2\xbf\x05\n\x03Msg\x12u\n\x0b\x43reateDenom\x12..injective.tokenfactory.v1beta1.MsgCreateDenom\x1a\x36.injective.tokenfactory.v1beta1.MsgCreateDenomResponse\x12`\n\x04Mint\x12\'.injective.tokenfactory.v1beta1.MsgMint\x1a/.injective.tokenfactory.v1beta1.MsgMintResponse\x12`\n\x04\x42urn\x12\'.injective.tokenfactory.v1beta1.MsgBurn\x1a/.injective.tokenfactory.v1beta1.MsgBurnResponse\x12u\n\x0b\x43hangeAdmin\x12..injective.tokenfactory.v1beta1.MsgChangeAdmin\x1a\x36.injective.tokenfactory.v1beta1.MsgChangeAdminResponse\x12\x84\x01\n\x10SetDenomMetadata\x12\x33.injective.tokenfactory.v1beta1.MsgSetDenomMetadata\x1a;.injective.tokenfactory.v1beta1.MsgSetDenomMetadataResponse\x12x\n\x0cUpdateParams\x12/.injective.tokenfactory.v1beta1.MsgUpdateParams\x1a\x37.injective.tokenfactory.v1beta1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01\x42\x9b\x02\n\"com.injective.tokenfactory.v1beta1B\x07TxProtoP\x01ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types\xa2\x02\x03ITX\xaa\x02\x1eInjective.Tokenfactory.V1beta1\xca\x02\x1eInjective\\Tokenfactory\\V1beta1\xe2\x02*Injective\\Tokenfactory\\V1beta1\\GPBMetadata\xea\x02 Injective::Tokenfactory::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.tokenfactory.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.injective.tokenfactory.v1beta1B\007TxProtoP\001ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types\242\002\003ITX\252\002\036Injective.Tokenfactory.V1beta1\312\002\036Injective\\Tokenfactory\\V1beta1\342\002*Injective\\Tokenfactory\\V1beta1\\GPBMetadata\352\002 Injective::Tokenfactory::V1beta1'
  _globals['_MSGCREATEDENOM'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGCREATEDENOM'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGCREATEDENOM'].fields_by_name['subdenom']._loaded_options = None
  _globals['_MSGCREATEDENOM'].fields_by_name['subdenom']._serialized_options = b'\362\336\037\017yaml:\"subdenom\"'
  _globals['_MSGCREATEDENOM'].fields_by_name['name']._loaded_options = None
  _globals['_MSGCREATEDENOM'].fields_by_name['name']._serialized_options = b'\362\336\037\013yaml:\"name\"'
  _globals['_MSGCREATEDENOM'].fields_by_name['symbol']._loaded_options = None
  _globals['_MSGCREATEDENOM'].fields_by_name['symbol']._serialized_options = b'\362\336\037\ryaml:\"symbol\"'
  _globals['_MSGCREATEDENOM'].fields_by_name['decimals']._loaded_options = None
  _globals['_MSGCREATEDENOM'].fields_by_name['decimals']._serialized_options = b'\362\336\037\017yaml:\"decimals\"'
  _globals['_MSGCREATEDENOM']._loaded_options = None
  _globals['_MSGCREATEDENOM']._serialized_options = b'\202\347\260*\006sender\212\347\260*#injective/tokenfactory/create-denom'
  _globals['_MSGCREATEDENOMRESPONSE'].fields_by_name['new_token_denom']._loaded_options = None
  _globals['_MSGCREATEDENOMRESPONSE'].fields_by_name['new_token_denom']._serialized_options = b'\362\336\037\026yaml:\"new_token_denom\"'
  _globals['_MSGMINT'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGMINT'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGMINT'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGMINT'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\362\336\037\ryaml:\"amount\"'
  _globals['_MSGMINT']._loaded_options = None
  _globals['_MSGMINT']._serialized_options = b'\202\347\260*\006sender\212\347\260*\033injective/tokenfactory/mint'
  _globals['_MSGBURN'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGBURN'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGBURN'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGBURN'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\362\336\037\ryaml:\"amount\"'
  _globals['_MSGBURN']._loaded_options = None
  _globals['_MSGBURN']._serialized_options = b'\202\347\260*\006sender\212\347\260*\033injective/tokenfactory/burn'
  _globals['_MSGCHANGEADMIN'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGCHANGEADMIN'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGCHANGEADMIN'].fields_by_name['denom']._loaded_options = None
  _globals['_MSGCHANGEADMIN'].fields_by_name['denom']._serialized_options = b'\362\336\037\014yaml:\"denom\"'
  _globals['_MSGCHANGEADMIN'].fields_by_name['new_admin']._loaded_options = None
  _globals['_MSGCHANGEADMIN'].fields_by_name['new_admin']._serialized_options = b'\362\336\037\020yaml:\"new_admin\"'
  _globals['_MSGCHANGEADMIN']._loaded_options = None
  _globals['_MSGCHANGEADMIN']._serialized_options = b'\202\347\260*\006sender\212\347\260*#injective/tokenfactory/change-admin'
  _globals['_MSGSETDENOMMETADATA'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGSETDENOMMETADATA'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGSETDENOMMETADATA'].fields_by_name['metadata']._loaded_options = None
  _globals['_MSGSETDENOMMETADATA'].fields_by_name['metadata']._serialized_options = b'\310\336\037\000\362\336\037\017yaml:\"metadata\"'
  _globals['_MSGSETDENOMMETADATA']._loaded_options = None
  _globals['_MSGSETDENOMMETADATA']._serialized_options = b'\202\347\260*\006sender\212\347\260*)injective/tokenfactory/set-denom-metadata'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*$injective/tokenfactory/update-params'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGCREATEDENOM']._serialized_start=278
  _globals['_MSGCREATEDENOM']._serialized_end=568
  _globals['_MSGCREATEDENOMRESPONSE']._serialized_start=570
  _globals['_MSGCREATEDENOMRESPONSE']._serialized_end=662
  _globals['_MSGMINT']._serialized_start=665
  _globals['_MSGMINT']._serialized_end=836
  _globals['_MSGMINTRESPONSE']._serialized_start=838
  _globals['_MSGMINTRESPONSE']._serialized_end=855
  _globals['_MSGBURN']._serialized_start=858
  _globals['_MSGBURN']._serialized_end=1029
  _globals['_MSGBURNRESPONSE']._serialized_start=1031
  _globals['_MSGBURNRESPONSE']._serialized_end=1048
  _globals['_MSGCHANGEADMIN']._serialized_start=1051
  _globals['_MSGCHANGEADMIN']._serialized_end=1254
  _globals['_MSGCHANGEADMINRESPONSE']._serialized_start=1256
  _globals['_MSGCHANGEADMINRESPONSE']._serialized_end=1280
  _globals['_MSGSETDENOMMETADATA']._serialized_start=1283
  _globals['_MSGSETDENOMMETADATA']._serialized_end=1490
  _globals['_MSGSETDENOMMETADATARESPONSE']._serialized_start=1492
  _globals['_MSGSETDENOMMETADATARESPONSE']._serialized_end=1521
  _globals['_MSGUPDATEPARAMS']._serialized_start=1524
  _globals['_MSGUPDATEPARAMS']._serialized_end=1724
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=1726
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=1751
  _globals['_MSG']._serialized_start=1754
  _globals['_MSG']._serialized_end=2457
# @@protoc_insertion_point(module_scope)
