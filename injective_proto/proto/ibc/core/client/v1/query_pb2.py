from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/client/v1/query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from injective_proto.proto.cosmos.query.v1 import query_pb2 as cosmos_dot_query_dot_v1_dot_query__pb2
from injective_proto.proto.ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from injective_proto.proto.ibc.core.commitment.v1 import commitment_pb2 as ibc_dot_core_dot_commitment_dot_v1_dot_commitment__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from injective_proto.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from injective_proto.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\x1eibc/core/client/v1/query.proto\x12\x12ibc.core.client.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1b\x63osmos/query/v1/query.proto\x1a\x1fibc/core/client/v1/client.proto\x1a\'ibc/core/commitment/v1/commitment.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x14gogoproto/gogo.proto\"6\n\x17QueryClientStateRequest\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\"\xae\x01\n\x18QueryClientStateResponse\x12\x37\n\x0c\x63lient_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyR\x0b\x63lientState\x12\x14\n\x05proof\x18\x02 \x01(\x0cR\x05proof\x12\x43\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0bproofHeight\"b\n\x18QueryClientStatesRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xd4\x01\n\x19QueryClientStatesResponse\x12n\n\rclient_states\x18\x01 \x03(\x0b\x32).ibc.core.client.v1.IdentifiedClientStateB\x1e\xc8\xde\x1f\x00\xaa\xdf\x1f\x16IdentifiedClientStatesR\x0c\x63lientStates\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"\xb0\x01\n\x1aQueryConsensusStateRequest\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12\'\n\x0frevision_number\x18\x02 \x01(\x04R\x0erevisionNumber\x12\'\n\x0frevision_height\x18\x03 \x01(\x04R\x0erevisionHeight\x12#\n\rlatest_height\x18\x04 \x01(\x08R\x0clatestHeight\"\xb7\x01\n\x1bQueryConsensusStateResponse\x12=\n\x0f\x63onsensus_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyR\x0e\x63onsensusState\x12\x14\n\x05proof\x18\x02 \x01(\x0cR\x05proof\x12\x43\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0bproofHeight\"\x82\x01\n\x1bQueryConsensusStatesRequest\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xc6\x01\n\x1cQueryConsensusStatesResponse\x12]\n\x10\x63onsensus_states\x18\x01 \x03(\x0b\x32,.ibc.core.client.v1.ConsensusStateWithHeightB\x04\xc8\xde\x1f\x00R\x0f\x63onsensusStates\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"\x88\x01\n!QueryConsensusStateHeightsRequest\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xc7\x01\n\"QueryConsensusStateHeightsResponse\x12X\n\x17\x63onsensus_state_heights\x18\x01 \x03(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x15\x63onsensusStateHeights\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"7\n\x18QueryClientStatusRequest\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\"3\n\x19QueryClientStatusResponse\x12\x16\n\x06status\x18\x01 \x01(\tR\x06status\"\x1a\n\x18QueryClientParamsRequest\"O\n\x19QueryClientParamsResponse\x12\x32\n\x06params\x18\x01 \x01(\x0b\x32\x1a.ibc.core.client.v1.ParamsR\x06params\"!\n\x1fQueryUpgradedClientStateRequest\"l\n QueryUpgradedClientStateResponse\x12H\n\x15upgraded_client_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyR\x13upgradedClientState\"$\n\"QueryUpgradedConsensusStateRequest\"u\n#QueryUpgradedConsensusStateResponse\x12N\n\x18upgraded_consensus_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyR\x16upgradedConsensusState\"\xb7\x02\n\x1cQueryVerifyMembershipRequest\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12\x14\n\x05proof\x18\x02 \x01(\x0cR\x05proof\x12\x43\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00R\x0bproofHeight\x12I\n\x0bmerkle_path\x18\x04 \x01(\x0b\x32\".ibc.core.commitment.v1.MerklePathB\x04\xc8\xde\x1f\x00R\nmerklePath\x12\x14\n\x05value\x18\x05 \x01(\x0cR\x05value\x12\x1d\n\ntime_delay\x18\x06 \x01(\x04R\ttimeDelay\x12\x1f\n\x0b\x62lock_delay\x18\x07 \x01(\x04R\nblockDelay\"9\n\x1dQueryVerifyMembershipResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success2\x82\x0e\n\x05Query\x12\x9f\x01\n\x0b\x43lientState\x12+.ibc.core.client.v1.QueryClientStateRequest\x1a,.ibc.core.client.v1.QueryClientStateResponse\"5\x82\xd3\xe4\x93\x02/\x12-/ibc/core/client/v1/client_states/{client_id}\x12\x96\x01\n\x0c\x43lientStates\x12,.ibc.core.client.v1.QueryClientStatesRequest\x1a-.ibc.core.client.v1.QueryClientStatesResponse\")\x82\xd3\xe4\x93\x02#\x12!/ibc/core/client/v1/client_states\x12\xdf\x01\n\x0e\x43onsensusState\x12..ibc.core.client.v1.QueryConsensusStateRequest\x1a/.ibc.core.client.v1.QueryConsensusStateResponse\"l\x82\xd3\xe4\x93\x02\x66\x12\x64/ibc/core/client/v1/consensus_states/{client_id}/revision/{revision_number}/height/{revision_height}\x12\xae\x01\n\x0f\x43onsensusStates\x12/.ibc.core.client.v1.QueryConsensusStatesRequest\x1a\x30.ibc.core.client.v1.QueryConsensusStatesResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/ibc/core/client/v1/consensus_states/{client_id}\x12\xc8\x01\n\x15\x43onsensusStateHeights\x12\x35.ibc.core.client.v1.QueryConsensusStateHeightsRequest\x1a\x36.ibc.core.client.v1.QueryConsensusStateHeightsResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/ibc/core/client/v1/consensus_states/{client_id}/heights\x12\xa2\x01\n\x0c\x43lientStatus\x12,.ibc.core.client.v1.QueryClientStatusRequest\x1a-.ibc.core.client.v1.QueryClientStatusResponse\"5\x82\xd3\xe4\x93\x02/\x12-/ibc/core/client/v1/client_status/{client_id}\x12\x8f\x01\n\x0c\x43lientParams\x12,.ibc.core.client.v1.QueryClientParamsRequest\x1a-.ibc.core.client.v1.QueryClientParamsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/ibc/core/client/v1/params\x12\xb4\x01\n\x13UpgradedClientState\x12\x33.ibc.core.client.v1.QueryUpgradedClientStateRequest\x1a\x34.ibc.core.client.v1.QueryUpgradedClientStateResponse\"2\x82\xd3\xe4\x93\x02,\x12*/ibc/core/client/v1/upgraded_client_states\x12\xc0\x01\n\x16UpgradedConsensusState\x12\x36.ibc.core.client.v1.QueryUpgradedConsensusStateRequest\x1a\x37.ibc.core.client.v1.QueryUpgradedConsensusStateResponse\"5\x82\xd3\xe4\x93\x02/\x12-/ibc/core/client/v1/upgraded_consensus_states\x12\xae\x01\n\x10VerifyMembership\x12\x30.ibc.core.client.v1.QueryVerifyMembershipRequest\x1a\x31.ibc.core.client.v1.QueryVerifyMembershipResponse\"5\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02*\"%/ibc/core/client/v1/verify_membership:\x01*B\xc9\x01\n\x16\x63om.ibc.core.client.v1B\nQueryProtoP\x01Z8github.com/cosmos/ibc-go/v8/modules/core/02-client/types\xa2\x02\x03ICC\xaa\x02\x12Ibc.Core.Client.V1\xca\x02\x12Ibc\\Core\\Client\\V1\xe2\x02\x1eIbc\\Core\\Client\\V1\\GPBMetadata\xea\x02\x15Ibc::Core::Client::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.client.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.ibc.core.client.v1B\nQueryProtoP\001Z8github.com/cosmos/ibc-go/v8/modules/core/02-client/types\242\002\003ICC\252\002\022Ibc.Core.Client.V1\312\002\022Ibc\\Core\\Client\\V1\342\002\036Ibc\\Core\\Client\\V1\\GPBMetadata\352\002\025Ibc::Core::Client::V1'
  _globals['_QUERYCLIENTSTATERESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYCLIENTSTATERESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYCLIENTSTATESRESPONSE'].fields_by_name['client_states']._loaded_options = None
  _globals['_QUERYCLIENTSTATESRESPONSE'].fields_by_name['client_states']._serialized_options = b'\310\336\037\000\252\337\037\026IdentifiedClientStates'
  _globals['_QUERYCONSENSUSSTATERESPONSE'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYCONSENSUSSTATERESPONSE'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYCONSENSUSSTATESRESPONSE'].fields_by_name['consensus_states']._loaded_options = None
  _globals['_QUERYCONSENSUSSTATESRESPONSE'].fields_by_name['consensus_states']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYCONSENSUSSTATEHEIGHTSRESPONSE'].fields_by_name['consensus_state_heights']._loaded_options = None
  _globals['_QUERYCONSENSUSSTATEHEIGHTSRESPONSE'].fields_by_name['consensus_state_heights']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYVERIFYMEMBERSHIPREQUEST'].fields_by_name['proof_height']._loaded_options = None
  _globals['_QUERYVERIFYMEMBERSHIPREQUEST'].fields_by_name['proof_height']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYVERIFYMEMBERSHIPREQUEST'].fields_by_name['merkle_path']._loaded_options = None
  _globals['_QUERYVERIFYMEMBERSHIPREQUEST'].fields_by_name['merkle_path']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['ClientState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ClientState']._serialized_options = b'\202\323\344\223\002/\022-/ibc/core/client/v1/client_states/{client_id}'
  _globals['_QUERY'].methods_by_name['ClientStates']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ClientStates']._serialized_options = b'\202\323\344\223\002#\022!/ibc/core/client/v1/client_states'
  _globals['_QUERY'].methods_by_name['ConsensusState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ConsensusState']._serialized_options = b'\202\323\344\223\002f\022d/ibc/core/client/v1/consensus_states/{client_id}/revision/{revision_number}/height/{revision_height}'
  _globals['_QUERY'].methods_by_name['ConsensusStates']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ConsensusStates']._serialized_options = b'\202\323\344\223\0022\0220/ibc/core/client/v1/consensus_states/{client_id}'
  _globals['_QUERY'].methods_by_name['ConsensusStateHeights']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ConsensusStateHeights']._serialized_options = b'\202\323\344\223\002:\0228/ibc/core/client/v1/consensus_states/{client_id}/heights'
  _globals['_QUERY'].methods_by_name['ClientStatus']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ClientStatus']._serialized_options = b'\202\323\344\223\002/\022-/ibc/core/client/v1/client_status/{client_id}'
  _globals['_QUERY'].methods_by_name['ClientParams']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ClientParams']._serialized_options = b'\202\323\344\223\002\034\022\032/ibc/core/client/v1/params'
  _globals['_QUERY'].methods_by_name['UpgradedClientState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['UpgradedClientState']._serialized_options = b'\202\323\344\223\002,\022*/ibc/core/client/v1/upgraded_client_states'
  _globals['_QUERY'].methods_by_name['UpgradedConsensusState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['UpgradedConsensusState']._serialized_options = b'\202\323\344\223\002/\022-/ibc/core/client/v1/upgraded_consensus_states'
  _globals['_QUERY'].methods_by_name['VerifyMembership']._loaded_options = None
  _globals['_QUERY'].methods_by_name['VerifyMembership']._serialized_options = b'\210\347\260*\001\202\323\344\223\002*\"%/ibc/core/client/v1/verify_membership:\001*'
  _globals['_QUERYCLIENTSTATEREQUEST']._serialized_start=280
  _globals['_QUERYCLIENTSTATEREQUEST']._serialized_end=334
  _globals['_QUERYCLIENTSTATERESPONSE']._serialized_start=337
  _globals['_QUERYCLIENTSTATERESPONSE']._serialized_end=511
  _globals['_QUERYCLIENTSTATESREQUEST']._serialized_start=513
  _globals['_QUERYCLIENTSTATESREQUEST']._serialized_end=611
  _globals['_QUERYCLIENTSTATESRESPONSE']._serialized_start=614
  _globals['_QUERYCLIENTSTATESRESPONSE']._serialized_end=826
  _globals['_QUERYCONSENSUSSTATEREQUEST']._serialized_start=829
  _globals['_QUERYCONSENSUSSTATEREQUEST']._serialized_end=1005
  _globals['_QUERYCONSENSUSSTATERESPONSE']._serialized_start=1008
  _globals['_QUERYCONSENSUSSTATERESPONSE']._serialized_end=1191
  _globals['_QUERYCONSENSUSSTATESREQUEST']._serialized_start=1194
  _globals['_QUERYCONSENSUSSTATESREQUEST']._serialized_end=1324
  _globals['_QUERYCONSENSUSSTATESRESPONSE']._serialized_start=1327
  _globals['_QUERYCONSENSUSSTATESRESPONSE']._serialized_end=1525
  _globals['_QUERYCONSENSUSSTATEHEIGHTSREQUEST']._serialized_start=1528
  _globals['_QUERYCONSENSUSSTATEHEIGHTSREQUEST']._serialized_end=1664
  _globals['_QUERYCONSENSUSSTATEHEIGHTSRESPONSE']._serialized_start=1667
  _globals['_QUERYCONSENSUSSTATEHEIGHTSRESPONSE']._serialized_end=1866
  _globals['_QUERYCLIENTSTATUSREQUEST']._serialized_start=1868
  _globals['_QUERYCLIENTSTATUSREQUEST']._serialized_end=1923
  _globals['_QUERYCLIENTSTATUSRESPONSE']._serialized_start=1925
  _globals['_QUERYCLIENTSTATUSRESPONSE']._serialized_end=1976
  _globals['_QUERYCLIENTPARAMSREQUEST']._serialized_start=1978
  _globals['_QUERYCLIENTPARAMSREQUEST']._serialized_end=2004
  _globals['_QUERYCLIENTPARAMSRESPONSE']._serialized_start=2006
  _globals['_QUERYCLIENTPARAMSRESPONSE']._serialized_end=2085
  _globals['_QUERYUPGRADEDCLIENTSTATEREQUEST']._serialized_start=2087
  _globals['_QUERYUPGRADEDCLIENTSTATEREQUEST']._serialized_end=2120
  _globals['_QUERYUPGRADEDCLIENTSTATERESPONSE']._serialized_start=2122
  _globals['_QUERYUPGRADEDCLIENTSTATERESPONSE']._serialized_end=2230
  _globals['_QUERYUPGRADEDCONSENSUSSTATEREQUEST']._serialized_start=2232
  _globals['_QUERYUPGRADEDCONSENSUSSTATEREQUEST']._serialized_end=2268
  _globals['_QUERYUPGRADEDCONSENSUSSTATERESPONSE']._serialized_start=2270
  _globals['_QUERYUPGRADEDCONSENSUSSTATERESPONSE']._serialized_end=2387
  _globals['_QUERYVERIFYMEMBERSHIPREQUEST']._serialized_start=2390
  _globals['_QUERYVERIFYMEMBERSHIPREQUEST']._serialized_end=2701
  _globals['_QUERYVERIFYMEMBERSHIPRESPONSE']._serialized_start=2703
  _globals['_QUERYVERIFYMEMBERSHIPRESPONSE']._serialized_end=2760
  _globals['_QUERY']._serialized_start=2763
  _globals['_QUERY']._serialized_end=4557
# @@protoc_insertion_point(module_scope)