from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1beta1/genesis.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from injective_proto.proto.cosmos.gov.v1beta1 import gov_pb2 as cosmos_dot_gov_dot_v1beta1_dot_gov__pb2
from injective_proto.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n cosmos/gov/v1beta1/genesis.proto\x12\x12\x63osmos.gov.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1c\x63osmos/gov/v1beta1/gov.proto\x1a\x11\x61mino/amino.proto\"\x9e\x04\n\x0cGenesisState\x12\x30\n\x14starting_proposal_id\x18\x01 \x01(\x04R\x12startingProposalId\x12N\n\x08\x64\x65posits\x18\x02 \x03(\x0b\x32\x1b.cosmos.gov.v1beta1.DepositB\x15\xc8\xde\x1f\x00\xaa\xdf\x1f\x08\x44\x65posits\xa8\xe7\xb0*\x01R\x08\x64\x65posits\x12\x42\n\x05votes\x18\x03 \x03(\x0b\x32\x18.cosmos.gov.v1beta1.VoteB\x12\xc8\xde\x1f\x00\xaa\xdf\x1f\x05Votes\xa8\xe7\xb0*\x01R\x05votes\x12R\n\tproposals\x18\x04 \x03(\x0b\x32\x1c.cosmos.gov.v1beta1.ProposalB\x16\xc8\xde\x1f\x00\xaa\xdf\x1f\tProposals\xa8\xe7\xb0*\x01R\tproposals\x12S\n\x0e\x64\x65posit_params\x18\x05 \x01(\x0b\x32!.cosmos.gov.v1beta1.DepositParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\rdepositParams\x12P\n\rvoting_params\x18\x06 \x01(\x0b\x32 .cosmos.gov.v1beta1.VotingParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x0cvotingParams\x12M\n\x0ctally_params\x18\x07 \x01(\x0b\x32\x1f.cosmos.gov.v1beta1.TallyParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x0btallyParamsB\xc2\x01\n\x16\x63om.cosmos.gov.v1beta1B\x0cGenesisProtoP\x01Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1\xa2\x02\x03\x43GX\xaa\x02\x12\x43osmos.Gov.V1beta1\xca\x02\x12\x43osmos\\Gov\\V1beta1\xe2\x02\x1e\x43osmos\\Gov\\V1beta1\\GPBMetadata\xea\x02\x14\x43osmos::Gov::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.gov.v1beta1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.cosmos.gov.v1beta1B\014GenesisProtoP\001Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1\242\002\003CGX\252\002\022Cosmos.Gov.V1beta1\312\002\022Cosmos\\Gov\\V1beta1\342\002\036Cosmos\\Gov\\V1beta1\\GPBMetadata\352\002\024Cosmos::Gov::V1beta1'
  _globals['_GENESISSTATE'].fields_by_name['deposits']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['deposits']._serialized_options = b'\310\336\037\000\252\337\037\010Deposits\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['votes']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['votes']._serialized_options = b'\310\336\037\000\252\337\037\005Votes\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['proposals']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['proposals']._serialized_options = b'\310\336\037\000\252\337\037\tProposals\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['deposit_params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['deposit_params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['voting_params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['voting_params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['tally_params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['tally_params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE']._serialized_start=128
  _globals['_GENESISSTATE']._serialized_end=670
# @@protoc_insertion_point(module_scope)