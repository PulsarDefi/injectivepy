from pyinjective.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/wasmx/v1/proposal.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.cosmwasm.wasm.v1 import proposal_legacy_pb2 as cosmwasm_dot_wasm_dot_v1_dot_proposal__legacy__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n!injective/wasmx/v1/proposal.proto\x12\x12injective.wasmx.v1\x1a\x19\x63osmos_proto/cosmos.proto\x1a&cosmwasm/wasm/v1/proposal_legacy.proto\x1a\x14gogoproto/gogo.proto\x1a\x11\x61mino/amino.proto\"\xae\x02\n#ContractRegistrationRequestProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12y\n\x1d\x63ontract_registration_request\x18\x03 \x01(\x0b\x32/.injective.wasmx.v1.ContractRegistrationRequestB\x04\xc8\xde\x1f\x00R\x1b\x63ontractRegistrationRequest:T\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*)wasmx/ContractRegistrationRequestProposal\"\xba\x02\n(BatchContractRegistrationRequestProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12{\n\x1e\x63ontract_registration_requests\x18\x03 \x03(\x0b\x32/.injective.wasmx.v1.ContractRegistrationRequestB\x04\xc8\xde\x1f\x00R\x1c\x63ontractRegistrationRequests:Y\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*.wasmx/BatchContractRegistrationRequestProposal\"\xd1\x01\n#BatchContractDeregistrationProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x1c\n\tcontracts\x18\x03 \x03(\tR\tcontracts:T\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*)wasmx/BatchContractDeregistrationProposal\"\xaf\x03\n\x1b\x43ontractRegistrationRequest\x12)\n\x10\x63ontract_address\x18\x01 \x01(\tR\x0f\x63ontractAddress\x12\x1b\n\tgas_limit\x18\x02 \x01(\x04R\x08gasLimit\x12\x1b\n\tgas_price\x18\x03 \x01(\x04R\x08gasPrice\x12.\n\x13should_pin_contract\x18\x04 \x01(\x08R\x11shouldPinContract\x12\x30\n\x14is_migration_allowed\x18\x05 \x01(\x08R\x12isMigrationAllowed\x12\x17\n\x07\x63ode_id\x18\x06 \x01(\x04R\x06\x63odeId\x12#\n\radmin_address\x18\x07 \x01(\tR\x0c\x61\x64minAddress\x12\'\n\x0fgranter_address\x18\x08 \x01(\tR\x0egranterAddress\x12\x42\n\x0c\x66unding_mode\x18\t \x01(\x0e\x32\x1f.injective.wasmx.v1.FundingModeR\x0b\x66undingMode:\x1e\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xe2\x01\n\x16\x42\x61tchStoreCodeProposal\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12G\n\tproposals\x18\x03 \x03(\x0b\x32#.cosmwasm.wasm.v1.StoreCodeProposalB\x04\xc8\xde\x1f\x00R\tproposals:G\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\x8a\xe7\xb0*\x1cwasmx/BatchStoreCodeProposal*G\n\x0b\x46undingMode\x12\x0f\n\x0bUnspecified\x10\x00\x12\x0e\n\nSelfFunded\x10\x01\x12\r\n\tGrantOnly\x10\x02\x12\x08\n\x04\x44ual\x10\x03\x42\xde\x01\n\x16\x63om.injective.wasmx.v1B\rProposalProtoP\x01ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/types\xa2\x02\x03IWX\xaa\x02\x12Injective.Wasmx.V1\xca\x02\x12Injective\\Wasmx\\V1\xe2\x02\x1eInjective\\Wasmx\\V1\\GPBMetadata\xea\x02\x14Injective::Wasmx::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.wasmx.v1.proposal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.injective.wasmx.v1B\rProposalProtoP\001ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/types\242\002\003IWX\252\002\022Injective.Wasmx.V1\312\002\022Injective\\Wasmx\\V1\342\002\036Injective\\Wasmx\\V1\\GPBMetadata\352\002\024Injective::Wasmx::V1'
  _globals['_CONTRACTREGISTRATIONREQUESTPROPOSAL'].fields_by_name['contract_registration_request']._loaded_options = None
  _globals['_CONTRACTREGISTRATIONREQUESTPROPOSAL'].fields_by_name['contract_registration_request']._serialized_options = b'\310\336\037\000'
  _globals['_CONTRACTREGISTRATIONREQUESTPROPOSAL']._loaded_options = None
  _globals['_CONTRACTREGISTRATIONREQUESTPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*)wasmx/ContractRegistrationRequestProposal'
  _globals['_BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL'].fields_by_name['contract_registration_requests']._loaded_options = None
  _globals['_BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL'].fields_by_name['contract_registration_requests']._serialized_options = b'\310\336\037\000'
  _globals['_BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL']._loaded_options = None
  _globals['_BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*.wasmx/BatchContractRegistrationRequestProposal'
  _globals['_BATCHCONTRACTDEREGISTRATIONPROPOSAL']._loaded_options = None
  _globals['_BATCHCONTRACTDEREGISTRATIONPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*)wasmx/BatchContractDeregistrationProposal'
  _globals['_CONTRACTREGISTRATIONREQUEST']._loaded_options = None
  _globals['_CONTRACTREGISTRATIONREQUEST']._serialized_options = b'\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_BATCHSTORECODEPROPOSAL'].fields_by_name['proposals']._loaded_options = None
  _globals['_BATCHSTORECODEPROPOSAL'].fields_by_name['proposals']._serialized_options = b'\310\336\037\000'
  _globals['_BATCHSTORECODEPROPOSAL']._loaded_options = None
  _globals['_BATCHSTORECODEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content\212\347\260*\034wasmx/BatchStoreCodeProposal'
  _globals['_FUNDINGMODE']._serialized_start=1662
  _globals['_FUNDINGMODE']._serialized_end=1733
  _globals['_CONTRACTREGISTRATIONREQUESTPROPOSAL']._serialized_start=166
  _globals['_CONTRACTREGISTRATIONREQUESTPROPOSAL']._serialized_end=468
  _globals['_BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL']._serialized_start=471
  _globals['_BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL']._serialized_end=785
  _globals['_BATCHCONTRACTDEREGISTRATIONPROPOSAL']._serialized_start=788
  _globals['_BATCHCONTRACTDEREGISTRATIONPROPOSAL']._serialized_end=997
  _globals['_CONTRACTREGISTRATIONREQUEST']._serialized_start=1000
  _globals['_CONTRACTREGISTRATIONREQUEST']._serialized_end=1431
  _globals['_BATCHSTORECODEPROPOSAL']._serialized_start=1434
  _globals['_BATCHSTORECODEPROPOSAL']._serialized_end=1660
# @@protoc_insertion_point(module_scope)
