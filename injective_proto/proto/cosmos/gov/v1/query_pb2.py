from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/gov/v1/query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from injective_proto.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from injective_proto.proto.cosmos.gov.v1 import gov_pb2 as cosmos_dot_gov_dot_v1_dot_gov__pb2
from injective_proto.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\x19\x63osmos/gov/v1/query.proto\x12\rcosmos.gov.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17\x63osmos/gov/v1/gov.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\x1a\n\x18QueryConstitutionRequest\"?\n\x19QueryConstitutionResponse\x12\"\n\x0c\x63onstitution\x18\x01 \x01(\tR\x0c\x63onstitution\"7\n\x14QueryProposalRequest\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x04R\nproposalId\"L\n\x15QueryProposalResponse\x12\x33\n\x08proposal\x18\x01 \x01(\x0b\x32\x17.cosmos.gov.v1.ProposalR\x08proposal\"\x8f\x02\n\x15QueryProposalsRequest\x12\x46\n\x0fproposal_status\x18\x01 \x01(\x0e\x32\x1d.cosmos.gov.v1.ProposalStatusR\x0eproposalStatus\x12.\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05voter\x12\x36\n\tdepositor\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tdepositor\x12\x46\n\npagination\x18\x04 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\x98\x01\n\x16QueryProposalsResponse\x12\x35\n\tproposals\x18\x01 \x03(\x0b\x32\x17.cosmos.gov.v1.ProposalR\tproposals\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"c\n\x10QueryVoteRequest\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x04R\nproposalId\x12.\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05voter\"<\n\x11QueryVoteResponse\x12\'\n\x04vote\x18\x01 \x01(\x0b\x32\x13.cosmos.gov.v1.VoteR\x04vote\"|\n\x11QueryVotesRequest\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x04R\nproposalId\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\x88\x01\n\x12QueryVotesResponse\x12)\n\x05votes\x18\x01 \x03(\x0b\x32\x13.cosmos.gov.v1.VoteR\x05votes\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"5\n\x12QueryParamsRequest\x12\x1f\n\x0bparams_type\x18\x01 \x01(\tR\nparamsType\"\x96\x02\n\x13QueryParamsResponse\x12\x44\n\rvoting_params\x18\x01 \x01(\x0b\x32\x1b.cosmos.gov.v1.VotingParamsB\x02\x18\x01R\x0cvotingParams\x12G\n\x0e\x64\x65posit_params\x18\x02 \x01(\x0b\x32\x1c.cosmos.gov.v1.DepositParamsB\x02\x18\x01R\rdepositParams\x12\x41\n\x0ctally_params\x18\x03 \x01(\x0b\x32\x1a.cosmos.gov.v1.TallyParamsB\x02\x18\x01R\x0btallyParams\x12-\n\x06params\x18\x04 \x01(\x0b\x32\x15.cosmos.gov.v1.ParamsR\x06params\"n\n\x13QueryDepositRequest\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x04R\nproposalId\x12\x36\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tdepositor\"H\n\x14QueryDepositResponse\x12\x30\n\x07\x64\x65posit\x18\x01 \x01(\x0b\x32\x16.cosmos.gov.v1.DepositR\x07\x64\x65posit\"\x7f\n\x14QueryDepositsRequest\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x04R\nproposalId\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\x94\x01\n\x15QueryDepositsResponse\x12\x32\n\x08\x64\x65posits\x18\x01 \x03(\x0b\x32\x16.cosmos.gov.v1.DepositR\x08\x64\x65posits\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\":\n\x17QueryTallyResultRequest\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x04R\nproposalId\"L\n\x18QueryTallyResultResponse\x12\x30\n\x05tally\x18\x01 \x01(\x0b\x32\x1a.cosmos.gov.v1.TallyResultR\x05tally2\xe3\t\n\x05Query\x12\x86\x01\n\x0c\x43onstitution\x12\'.cosmos.gov.v1.QueryConstitutionRequest\x1a(.cosmos.gov.v1.QueryConstitutionResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/gov/v1/constitution\x12\x85\x01\n\x08Proposal\x12#.cosmos.gov.v1.QueryProposalRequest\x1a$.cosmos.gov.v1.QueryProposalResponse\".\x82\xd3\xe4\x93\x02(\x12&/cosmos/gov/v1/proposals/{proposal_id}\x12z\n\tProposals\x12$.cosmos.gov.v1.QueryProposalsRequest\x1a%.cosmos.gov.v1.QueryProposalsResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/cosmos/gov/v1/proposals\x12\x87\x01\n\x04Vote\x12\x1f.cosmos.gov.v1.QueryVoteRequest\x1a .cosmos.gov.v1.QueryVoteResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/cosmos/gov/v1/proposals/{proposal_id}/votes/{voter}\x12\x82\x01\n\x05Votes\x12 .cosmos.gov.v1.QueryVotesRequest\x1a!.cosmos.gov.v1.QueryVotesResponse\"4\x82\xd3\xe4\x93\x02.\x12,/cosmos/gov/v1/proposals/{proposal_id}/votes\x12|\n\x06Params\x12!.cosmos.gov.v1.QueryParamsRequest\x1a\".cosmos.gov.v1.QueryParamsResponse\"+\x82\xd3\xe4\x93\x02%\x12#/cosmos/gov/v1/params/{params_type}\x12\x97\x01\n\x07\x44\x65posit\x12\".cosmos.gov.v1.QueryDepositRequest\x1a#.cosmos.gov.v1.QueryDepositResponse\"C\x82\xd3\xe4\x93\x02=\x12;/cosmos/gov/v1/proposals/{proposal_id}/deposits/{depositor}\x12\x8e\x01\n\x08\x44\x65posits\x12#.cosmos.gov.v1.QueryDepositsRequest\x1a$.cosmos.gov.v1.QueryDepositsResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//cosmos/gov/v1/proposals/{proposal_id}/deposits\x12\x94\x01\n\x0bTallyResult\x12&.cosmos.gov.v1.QueryTallyResultRequest\x1a\'.cosmos.gov.v1.QueryTallyResultResponse\"4\x82\xd3\xe4\x93\x02.\x12,/cosmos/gov/v1/proposals/{proposal_id}/tallyB\xa2\x01\n\x11\x63om.cosmos.gov.v1B\nQueryProtoP\x01Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1\xa2\x02\x03\x43GX\xaa\x02\rCosmos.Gov.V1\xca\x02\rCosmos\\Gov\\V1\xe2\x02\x19\x43osmos\\Gov\\V1\\GPBMetadata\xea\x02\x0f\x43osmos::Gov::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.gov.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.cosmos.gov.v1B\nQueryProtoP\001Z+github.com/cosmos/cosmos-sdk/x/gov/types/v1\242\002\003CGX\252\002\rCosmos.Gov.V1\312\002\rCosmos\\Gov\\V1\342\002\031Cosmos\\Gov\\V1\\GPBMetadata\352\002\017Cosmos::Gov::V1'
  _globals['_QUERYPROPOSALSREQUEST'].fields_by_name['voter']._loaded_options = None
  _globals['_QUERYPROPOSALSREQUEST'].fields_by_name['voter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYPROPOSALSREQUEST'].fields_by_name['depositor']._loaded_options = None
  _globals['_QUERYPROPOSALSREQUEST'].fields_by_name['depositor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYVOTEREQUEST'].fields_by_name['voter']._loaded_options = None
  _globals['_QUERYVOTEREQUEST'].fields_by_name['voter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['voting_params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['voting_params']._serialized_options = b'\030\001'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['deposit_params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['deposit_params']._serialized_options = b'\030\001'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['tally_params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['tally_params']._serialized_options = b'\030\001'
  _globals['_QUERYDEPOSITREQUEST'].fields_by_name['depositor']._loaded_options = None
  _globals['_QUERYDEPOSITREQUEST'].fields_by_name['depositor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERY'].methods_by_name['Constitution']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Constitution']._serialized_options = b'\202\323\344\223\002\035\022\033/cosmos/gov/v1/constitution'
  _globals['_QUERY'].methods_by_name['Proposal']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Proposal']._serialized_options = b'\202\323\344\223\002(\022&/cosmos/gov/v1/proposals/{proposal_id}'
  _globals['_QUERY'].methods_by_name['Proposals']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Proposals']._serialized_options = b'\202\323\344\223\002\032\022\030/cosmos/gov/v1/proposals'
  _globals['_QUERY'].methods_by_name['Vote']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Vote']._serialized_options = b'\202\323\344\223\0026\0224/cosmos/gov/v1/proposals/{proposal_id}/votes/{voter}'
  _globals['_QUERY'].methods_by_name['Votes']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Votes']._serialized_options = b'\202\323\344\223\002.\022,/cosmos/gov/v1/proposals/{proposal_id}/votes'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002%\022#/cosmos/gov/v1/params/{params_type}'
  _globals['_QUERY'].methods_by_name['Deposit']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Deposit']._serialized_options = b'\202\323\344\223\002=\022;/cosmos/gov/v1/proposals/{proposal_id}/deposits/{depositor}'
  _globals['_QUERY'].methods_by_name['Deposits']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Deposits']._serialized_options = b'\202\323\344\223\0021\022//cosmos/gov/v1/proposals/{proposal_id}/deposits'
  _globals['_QUERY'].methods_by_name['TallyResult']._loaded_options = None
  _globals['_QUERY'].methods_by_name['TallyResult']._serialized_options = b'\202\323\344\223\002.\022,/cosmos/gov/v1/proposals/{proposal_id}/tally'
  _globals['_QUERYCONSTITUTIONREQUEST']._serialized_start=170
  _globals['_QUERYCONSTITUTIONREQUEST']._serialized_end=196
  _globals['_QUERYCONSTITUTIONRESPONSE']._serialized_start=198
  _globals['_QUERYCONSTITUTIONRESPONSE']._serialized_end=261
  _globals['_QUERYPROPOSALREQUEST']._serialized_start=263
  _globals['_QUERYPROPOSALREQUEST']._serialized_end=318
  _globals['_QUERYPROPOSALRESPONSE']._serialized_start=320
  _globals['_QUERYPROPOSALRESPONSE']._serialized_end=396
  _globals['_QUERYPROPOSALSREQUEST']._serialized_start=399
  _globals['_QUERYPROPOSALSREQUEST']._serialized_end=670
  _globals['_QUERYPROPOSALSRESPONSE']._serialized_start=673
  _globals['_QUERYPROPOSALSRESPONSE']._serialized_end=825
  _globals['_QUERYVOTEREQUEST']._serialized_start=827
  _globals['_QUERYVOTEREQUEST']._serialized_end=926
  _globals['_QUERYVOTERESPONSE']._serialized_start=928
  _globals['_QUERYVOTERESPONSE']._serialized_end=988
  _globals['_QUERYVOTESREQUEST']._serialized_start=990
  _globals['_QUERYVOTESREQUEST']._serialized_end=1114
  _globals['_QUERYVOTESRESPONSE']._serialized_start=1117
  _globals['_QUERYVOTESRESPONSE']._serialized_end=1253
  _globals['_QUERYPARAMSREQUEST']._serialized_start=1255
  _globals['_QUERYPARAMSREQUEST']._serialized_end=1308
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=1311
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=1589
  _globals['_QUERYDEPOSITREQUEST']._serialized_start=1591
  _globals['_QUERYDEPOSITREQUEST']._serialized_end=1701
  _globals['_QUERYDEPOSITRESPONSE']._serialized_start=1703
  _globals['_QUERYDEPOSITRESPONSE']._serialized_end=1775
  _globals['_QUERYDEPOSITSREQUEST']._serialized_start=1777
  _globals['_QUERYDEPOSITSREQUEST']._serialized_end=1904
  _globals['_QUERYDEPOSITSRESPONSE']._serialized_start=1907
  _globals['_QUERYDEPOSITSRESPONSE']._serialized_end=2055
  _globals['_QUERYTALLYRESULTREQUEST']._serialized_start=2057
  _globals['_QUERYTALLYRESULTREQUEST']._serialized_end=2115
  _globals['_QUERYTALLYRESULTRESPONSE']._serialized_start=2117
  _globals['_QUERYTALLYRESULTRESPONSE']._serialized_end=2193
  _globals['_QUERY']._serialized_start=2196
  _globals['_QUERY']._serialized_end=3447
# @@protoc_insertion_point(module_scope)