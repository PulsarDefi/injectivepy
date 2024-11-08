from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/auction/v1beta1/tx.proto
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
from injective_proto.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from injective_proto.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from injective_proto.proto.injective.auction.v1beta1 import auction_pb2 as injective_dot_auction_dot_v1beta1_dot_auction__pb2
from injective_proto.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\"injective/auction/v1beta1/tx.proto\x12\x19injective.auction.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\'injective/auction/v1beta1/auction.proto\x1a\x11\x61mino/amino.proto\"\x9e\x01\n\x06MsgBid\x12\x16\n\x06sender\x18\x01 \x01(\tR\x06sender\x12>\n\nbid_amount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00R\tbidAmount\x12\x14\n\x05round\x18\x03 \x01(\x04R\x05round:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x0e\x61uction/MsgBid\"\x10\n\x0eMsgBidResponse\"\xb6\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12?\n\x06params\x18\x02 \x01(\x0b\x32!.injective.auction.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params:*\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x17\x61uction/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse2\xd1\x01\n\x03Msg\x12S\n\x03\x42id\x12!.injective.auction.v1beta1.MsgBid\x1a).injective.auction.v1beta1.MsgBidResponse\x12n\n\x0cUpdateParams\x12*.injective.auction.v1beta1.MsgUpdateParams\x1a\x32.injective.auction.v1beta1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01\x42\xfd\x01\n\x1d\x63om.injective.auction.v1beta1B\x07TxProtoP\x01ZMgithub.com/InjectiveLabs/injective-core/injective-chain/modules/auction/types\xa2\x02\x03IAX\xaa\x02\x19Injective.Auction.V1beta1\xca\x02\x19Injective\\Auction\\V1beta1\xe2\x02%Injective\\Auction\\V1beta1\\GPBMetadata\xea\x02\x1bInjective::Auction::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.auction.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.injective.auction.v1beta1B\007TxProtoP\001ZMgithub.com/InjectiveLabs/injective-core/injective-chain/modules/auction/types\242\002\003IAX\252\002\031Injective.Auction.V1beta1\312\002\031Injective\\Auction\\V1beta1\342\002%Injective\\Auction\\V1beta1\\GPBMetadata\352\002\033Injective::Auction::V1beta1'
  _globals['_MSGBID'].fields_by_name['bid_amount']._loaded_options = None
  _globals['_MSGBID'].fields_by_name['bid_amount']._serialized_options = b'\310\336\037\000'
  _globals['_MSGBID']._loaded_options = None
  _globals['_MSGBID']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender\212\347\260*\016auction/MsgBid'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\027auction/MsgUpdateParams'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGBID']._serialized_start=232
  _globals['_MSGBID']._serialized_end=390
  _globals['_MSGBIDRESPONSE']._serialized_start=392
  _globals['_MSGBIDRESPONSE']._serialized_end=408
  _globals['_MSGUPDATEPARAMS']._serialized_start=411
  _globals['_MSGUPDATEPARAMS']._serialized_end=593
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=595
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=620
  _globals['_MSG']._serialized_start=623
  _globals['_MSG']._serialized_end=832
# @@protoc_insertion_point(module_scope)
