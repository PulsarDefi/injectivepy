from pyinjective.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmwasm/wasm/v1/query.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmwasm.wasm.v1 import types_pb2 as cosmwasm_dot_wasm_dot_v1_dot_types__pb2
from pyinjective.proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from pyinjective.proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n\x1c\x63osmwasm/wasm/v1/query.proto\x12\x10\x63osmwasm.wasm.v1\x1a\x14gogoproto/gogo.proto\x1a\x1c\x63osmwasm/wasm/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x11\x61mino/amino.proto\x1a\x19\x63osmos_proto/cosmos.proto\"N\n\x18QueryContractInfoRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\"\xad\x01\n\x19QueryContractInfoResponse\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12V\n\rcontract_info\x18\x02 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.ContractInfoB\x11\xc8\xde\x1f\x00\xd0\xde\x1f\x01\xea\xde\x1f\x00\xa8\xe7\xb0*\x01R\x0c\x63ontractInfo:\x04\xe8\xa0\x1f\x01\"\x99\x01\n\x1bQueryContractHistoryRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xb8\x01\n\x1cQueryContractHistoryResponse\x12O\n\x07\x65ntries\x18\x01 \x03(\x0b\x32*.cosmwasm.wasm.v1.ContractCodeHistoryEntryB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x07\x65ntries\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"~\n\x1bQueryContractsByCodeRequest\x12\x17\n\x07\x63ode_id\x18\x01 \x01(\x04R\x06\x63odeId\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\x9f\x01\n\x1cQueryContractsByCodeResponse\x12\x36\n\tcontracts\x18\x01 \x03(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tcontracts\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"\x9a\x01\n\x1cQueryAllContractStateRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xa4\x01\n\x1dQueryAllContractStateResponse\x12:\n\x06models\x18\x01 \x03(\x0b\x32\x17.cosmwasm.wasm.v1.ModelB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06models\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"q\n\x1cQueryRawContractStateRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x1d\n\nquery_data\x18\x02 \x01(\x0cR\tqueryData\"3\n\x1dQueryRawContractStateResponse\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\"\x9b\x01\n\x1eQuerySmartContractStateRequest\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x45\n\nquery_data\x18\x02 \x01(\x0c\x42&\xfa\xde\x1f\x12RawContractMessage\x9a\xe7\xb0*\x0binline_jsonR\tqueryData\"]\n\x1fQuerySmartContractStateResponse\x12:\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x42&\xfa\xde\x1f\x12RawContractMessage\x9a\xe7\xb0*\x0binline_jsonR\x04\x64\x61ta\"+\n\x10QueryCodeRequest\x12\x17\n\x07\x63ode_id\x18\x01 \x01(\x04R\x06\x63odeId\"\xb8\x02\n\x10\x43odeInfoResponse\x12)\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\x10\xe2\xde\x1f\x06\x43odeID\xea\xde\x1f\x02idR\x06\x63odeId\x12\x32\n\x07\x63reator\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x63reator\x12Q\n\tdata_hash\x18\x03 \x01(\x0c\x42\x34\xfa\xde\x1f\x30github.com/cometbft/cometbft/libs/bytes.HexBytesR\x08\x64\x61taHash\x12`\n\x16instantiate_permission\x18\x06 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfigB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x15instantiatePermission:\x04\xe8\xa0\x1f\x01J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06\"\x82\x01\n\x11QueryCodeResponse\x12I\n\tcode_info\x18\x01 \x01(\x0b\x32\".cosmwasm.wasm.v1.CodeInfoResponseB\x08\xd0\xde\x1f\x01\xea\xde\x1f\x00R\x08\x63odeInfo\x12\x1c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x42\x08\xea\xde\x1f\x04\x64\x61taR\x04\x64\x61ta:\x04\xe8\xa0\x1f\x01\"[\n\x11QueryCodesRequest\x12\x46\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xab\x01\n\x12QueryCodesResponse\x12L\n\ncode_infos\x18\x01 \x03(\x0b\x32\".cosmwasm.wasm.v1.CodeInfoResponseB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\tcodeInfos\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"a\n\x17QueryPinnedCodesRequest\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\x8b\x01\n\x18QueryPinnedCodesResponse\x12&\n\x08\x63ode_ids\x18\x01 \x03(\x04\x42\x0b\xe2\xde\x1f\x07\x43odeIDsR\x07\x63odeIds\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"\x14\n\x12QueryParamsRequest\"R\n\x13QueryParamsResponse\x12;\n\x06params\x18\x01 \x01(\x0b\x32\x18.cosmwasm.wasm.v1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params\"\xab\x01\n\x1eQueryContractsByCreatorRequest\x12\x41\n\x0f\x63reator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x0e\x63reatorAddress\x12\x46\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequestR\npagination\"\xb3\x01\n\x1fQueryContractsByCreatorResponse\x12G\n\x12\x63ontract_addresses\x18\x01 \x03(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x11\x63ontractAddresses\x12G\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponseR\npagination\"\xab\x01\n\x18QueryBuildAddressRequest\x12\x1b\n\tcode_hash\x18\x01 \x01(\tR\x08\x63odeHash\x12\x41\n\x0f\x63reator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x0e\x63reatorAddress\x12\x12\n\x04salt\x18\x03 \x01(\tR\x04salt\x12\x1b\n\tinit_args\x18\x04 \x01(\x0cR\x08initArgs\"O\n\x19QueryBuildAddressResponse\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress2\xdf\x0e\n\x05Query\x12\x95\x01\n\x0c\x43ontractInfo\x12*.cosmwasm.wasm.v1.QueryContractInfoRequest\x1a+.cosmwasm.wasm.v1.QueryContractInfoResponse\",\x82\xd3\xe4\x93\x02&\x12$/cosmwasm/wasm/v1/contract/{address}\x12\xa6\x01\n\x0f\x43ontractHistory\x12-.cosmwasm.wasm.v1.QueryContractHistoryRequest\x1a..cosmwasm.wasm.v1.QueryContractHistoryResponse\"4\x82\xd3\xe4\x93\x02.\x12,/cosmwasm/wasm/v1/contract/{address}/history\x12\xa4\x01\n\x0f\x43ontractsByCode\x12-.cosmwasm.wasm.v1.QueryContractsByCodeRequest\x1a..cosmwasm.wasm.v1.QueryContractsByCodeResponse\"2\x82\xd3\xe4\x93\x02,\x12*/cosmwasm/wasm/v1/code/{code_id}/contracts\x12\xa7\x01\n\x10\x41llContractState\x12..cosmwasm.wasm.v1.QueryAllContractStateRequest\x1a/.cosmwasm.wasm.v1.QueryAllContractStateResponse\"2\x82\xd3\xe4\x93\x02,\x12*/cosmwasm/wasm/v1/contract/{address}/state\x12\xb2\x01\n\x10RawContractState\x12..cosmwasm.wasm.v1.QueryRawContractStateRequest\x1a/.cosmwasm.wasm.v1.QueryRawContractStateResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/cosmwasm/wasm/v1/contract/{address}/raw/{query_data}\x12\xba\x01\n\x12SmartContractState\x12\x30.cosmwasm.wasm.v1.QuerySmartContractStateRequest\x1a\x31.cosmwasm.wasm.v1.QuerySmartContractStateResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/cosmwasm/wasm/v1/contract/{address}/smart/{query_data}\x12y\n\x04\x43ode\x12\".cosmwasm.wasm.v1.QueryCodeRequest\x1a#.cosmwasm.wasm.v1.QueryCodeResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /cosmwasm/wasm/v1/code/{code_id}\x12r\n\x05\x43odes\x12#.cosmwasm.wasm.v1.QueryCodesRequest\x1a$.cosmwasm.wasm.v1.QueryCodesResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/cosmwasm/wasm/v1/code\x12\x8c\x01\n\x0bPinnedCodes\x12).cosmwasm.wasm.v1.QueryPinnedCodesRequest\x1a*.cosmwasm.wasm.v1.QueryPinnedCodesResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/cosmwasm/wasm/v1/codes/pinned\x12}\n\x06Params\x12$.cosmwasm.wasm.v1.QueryParamsRequest\x1a%.cosmwasm.wasm.v1.QueryParamsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/cosmwasm/wasm/v1/codes/params\x12\xb8\x01\n\x12\x43ontractsByCreator\x12\x30.cosmwasm.wasm.v1.QueryContractsByCreatorRequest\x1a\x31.cosmwasm.wasm.v1.QueryContractsByCreatorResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/cosmwasm/wasm/v1/contracts/creator/{creator_address}\x12\x99\x01\n\x0c\x42uildAddress\x12*.cosmwasm.wasm.v1.QueryBuildAddressRequest\x1a+.cosmwasm.wasm.v1.QueryBuildAddressResponse\"0\x82\xd3\xe4\x93\x02*\x12(/cosmwasm/wasm/v1/contract/build_addressB\xb4\x01\n\x14\x63om.cosmwasm.wasm.v1B\nQueryProtoP\x01Z&github.com/CosmWasm/wasmd/x/wasm/types\xa2\x02\x03\x43WX\xaa\x02\x10\x43osmwasm.Wasm.V1\xca\x02\x10\x43osmwasm\\Wasm\\V1\xe2\x02\x1c\x43osmwasm\\Wasm\\V1\\GPBMetadata\xea\x02\x12\x43osmwasm::Wasm::V1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmwasm.wasm.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.cosmwasm.wasm.v1B\nQueryProtoP\001Z&github.com/CosmWasm/wasmd/x/wasm/types\242\002\003CWX\252\002\020Cosmwasm.Wasm.V1\312\002\020Cosmwasm\\Wasm\\V1\342\002\034Cosmwasm\\Wasm\\V1\\GPBMetadata\352\002\022Cosmwasm::Wasm::V1\310\341\036\000\250\342\036\000'
  _globals['_QUERYCONTRACTINFOREQUEST'].fields_by_name['address']._loaded_options = None
  _globals['_QUERYCONTRACTINFOREQUEST'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYCONTRACTINFORESPONSE'].fields_by_name['address']._loaded_options = None
  _globals['_QUERYCONTRACTINFORESPONSE'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYCONTRACTINFORESPONSE'].fields_by_name['contract_info']._loaded_options = None
  _globals['_QUERYCONTRACTINFORESPONSE'].fields_by_name['contract_info']._serialized_options = b'\310\336\037\000\320\336\037\001\352\336\037\000\250\347\260*\001'
  _globals['_QUERYCONTRACTINFORESPONSE']._loaded_options = None
  _globals['_QUERYCONTRACTINFORESPONSE']._serialized_options = b'\350\240\037\001'
  _globals['_QUERYCONTRACTHISTORYREQUEST'].fields_by_name['address']._loaded_options = None
  _globals['_QUERYCONTRACTHISTORYREQUEST'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYCONTRACTHISTORYRESPONSE'].fields_by_name['entries']._loaded_options = None
  _globals['_QUERYCONTRACTHISTORYRESPONSE'].fields_by_name['entries']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_QUERYCONTRACTSBYCODERESPONSE'].fields_by_name['contracts']._loaded_options = None
  _globals['_QUERYCONTRACTSBYCODERESPONSE'].fields_by_name['contracts']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYALLCONTRACTSTATEREQUEST'].fields_by_name['address']._loaded_options = None
  _globals['_QUERYALLCONTRACTSTATEREQUEST'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYALLCONTRACTSTATERESPONSE'].fields_by_name['models']._loaded_options = None
  _globals['_QUERYALLCONTRACTSTATERESPONSE'].fields_by_name['models']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_QUERYRAWCONTRACTSTATEREQUEST'].fields_by_name['address']._loaded_options = None
  _globals['_QUERYRAWCONTRACTSTATEREQUEST'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYSMARTCONTRACTSTATEREQUEST'].fields_by_name['address']._loaded_options = None
  _globals['_QUERYSMARTCONTRACTSTATEREQUEST'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYSMARTCONTRACTSTATEREQUEST'].fields_by_name['query_data']._loaded_options = None
  _globals['_QUERYSMARTCONTRACTSTATEREQUEST'].fields_by_name['query_data']._serialized_options = b'\372\336\037\022RawContractMessage\232\347\260*\013inline_json'
  _globals['_QUERYSMARTCONTRACTSTATERESPONSE'].fields_by_name['data']._loaded_options = None
  _globals['_QUERYSMARTCONTRACTSTATERESPONSE'].fields_by_name['data']._serialized_options = b'\372\336\037\022RawContractMessage\232\347\260*\013inline_json'
  _globals['_CODEINFORESPONSE'].fields_by_name['code_id']._loaded_options = None
  _globals['_CODEINFORESPONSE'].fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID\352\336\037\002id'
  _globals['_CODEINFORESPONSE'].fields_by_name['creator']._loaded_options = None
  _globals['_CODEINFORESPONSE'].fields_by_name['creator']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_CODEINFORESPONSE'].fields_by_name['data_hash']._loaded_options = None
  _globals['_CODEINFORESPONSE'].fields_by_name['data_hash']._serialized_options = b'\372\336\0370github.com/cometbft/cometbft/libs/bytes.HexBytes'
  _globals['_CODEINFORESPONSE'].fields_by_name['instantiate_permission']._loaded_options = None
  _globals['_CODEINFORESPONSE'].fields_by_name['instantiate_permission']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_CODEINFORESPONSE']._loaded_options = None
  _globals['_CODEINFORESPONSE']._serialized_options = b'\350\240\037\001'
  _globals['_QUERYCODERESPONSE'].fields_by_name['code_info']._loaded_options = None
  _globals['_QUERYCODERESPONSE'].fields_by_name['code_info']._serialized_options = b'\320\336\037\001\352\336\037\000'
  _globals['_QUERYCODERESPONSE'].fields_by_name['data']._loaded_options = None
  _globals['_QUERYCODERESPONSE'].fields_by_name['data']._serialized_options = b'\352\336\037\004data'
  _globals['_QUERYCODERESPONSE']._loaded_options = None
  _globals['_QUERYCODERESPONSE']._serialized_options = b'\350\240\037\001'
  _globals['_QUERYCODESRESPONSE'].fields_by_name['code_infos']._loaded_options = None
  _globals['_QUERYCODESRESPONSE'].fields_by_name['code_infos']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_QUERYPINNEDCODESRESPONSE'].fields_by_name['code_ids']._loaded_options = None
  _globals['_QUERYPINNEDCODESRESPONSE'].fields_by_name['code_ids']._serialized_options = b'\342\336\037\007CodeIDs'
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
  _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_QUERYCONTRACTSBYCREATORREQUEST'].fields_by_name['creator_address']._loaded_options = None
  _globals['_QUERYCONTRACTSBYCREATORREQUEST'].fields_by_name['creator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYCONTRACTSBYCREATORRESPONSE'].fields_by_name['contract_addresses']._loaded_options = None
  _globals['_QUERYCONTRACTSBYCREATORRESPONSE'].fields_by_name['contract_addresses']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYBUILDADDRESSREQUEST'].fields_by_name['creator_address']._loaded_options = None
  _globals['_QUERYBUILDADDRESSREQUEST'].fields_by_name['creator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERYBUILDADDRESSRESPONSE'].fields_by_name['address']._loaded_options = None
  _globals['_QUERYBUILDADDRESSRESPONSE'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_QUERY'].methods_by_name['ContractInfo']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ContractInfo']._serialized_options = b'\202\323\344\223\002&\022$/cosmwasm/wasm/v1/contract/{address}'
  _globals['_QUERY'].methods_by_name['ContractHistory']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ContractHistory']._serialized_options = b'\202\323\344\223\002.\022,/cosmwasm/wasm/v1/contract/{address}/history'
  _globals['_QUERY'].methods_by_name['ContractsByCode']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ContractsByCode']._serialized_options = b'\202\323\344\223\002,\022*/cosmwasm/wasm/v1/code/{code_id}/contracts'
  _globals['_QUERY'].methods_by_name['AllContractState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['AllContractState']._serialized_options = b'\202\323\344\223\002,\022*/cosmwasm/wasm/v1/contract/{address}/state'
  _globals['_QUERY'].methods_by_name['RawContractState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['RawContractState']._serialized_options = b'\202\323\344\223\0027\0225/cosmwasm/wasm/v1/contract/{address}/raw/{query_data}'
  _globals['_QUERY'].methods_by_name['SmartContractState']._loaded_options = None
  _globals['_QUERY'].methods_by_name['SmartContractState']._serialized_options = b'\202\323\344\223\0029\0227/cosmwasm/wasm/v1/contract/{address}/smart/{query_data}'
  _globals['_QUERY'].methods_by_name['Code']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Code']._serialized_options = b'\202\323\344\223\002\"\022 /cosmwasm/wasm/v1/code/{code_id}'
  _globals['_QUERY'].methods_by_name['Codes']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Codes']._serialized_options = b'\202\323\344\223\002\030\022\026/cosmwasm/wasm/v1/code'
  _globals['_QUERY'].methods_by_name['PinnedCodes']._loaded_options = None
  _globals['_QUERY'].methods_by_name['PinnedCodes']._serialized_options = b'\202\323\344\223\002 \022\036/cosmwasm/wasm/v1/codes/pinned'
  _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
  _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\202\323\344\223\002 \022\036/cosmwasm/wasm/v1/codes/params'
  _globals['_QUERY'].methods_by_name['ContractsByCreator']._loaded_options = None
  _globals['_QUERY'].methods_by_name['ContractsByCreator']._serialized_options = b'\202\323\344\223\0027\0225/cosmwasm/wasm/v1/contracts/creator/{creator_address}'
  _globals['_QUERY'].methods_by_name['BuildAddress']._loaded_options = None
  _globals['_QUERY'].methods_by_name['BuildAddress']._serialized_options = b'\202\323\344\223\002*\022(/cosmwasm/wasm/v1/contract/build_address'
  _globals['_QUERYCONTRACTINFOREQUEST']._serialized_start=222
  _globals['_QUERYCONTRACTINFOREQUEST']._serialized_end=300
  _globals['_QUERYCONTRACTINFORESPONSE']._serialized_start=303
  _globals['_QUERYCONTRACTINFORESPONSE']._serialized_end=476
  _globals['_QUERYCONTRACTHISTORYREQUEST']._serialized_start=479
  _globals['_QUERYCONTRACTHISTORYREQUEST']._serialized_end=632
  _globals['_QUERYCONTRACTHISTORYRESPONSE']._serialized_start=635
  _globals['_QUERYCONTRACTHISTORYRESPONSE']._serialized_end=819
  _globals['_QUERYCONTRACTSBYCODEREQUEST']._serialized_start=821
  _globals['_QUERYCONTRACTSBYCODEREQUEST']._serialized_end=947
  _globals['_QUERYCONTRACTSBYCODERESPONSE']._serialized_start=950
  _globals['_QUERYCONTRACTSBYCODERESPONSE']._serialized_end=1109
  _globals['_QUERYALLCONTRACTSTATEREQUEST']._serialized_start=1112
  _globals['_QUERYALLCONTRACTSTATEREQUEST']._serialized_end=1266
  _globals['_QUERYALLCONTRACTSTATERESPONSE']._serialized_start=1269
  _globals['_QUERYALLCONTRACTSTATERESPONSE']._serialized_end=1433
  _globals['_QUERYRAWCONTRACTSTATEREQUEST']._serialized_start=1435
  _globals['_QUERYRAWCONTRACTSTATEREQUEST']._serialized_end=1548
  _globals['_QUERYRAWCONTRACTSTATERESPONSE']._serialized_start=1550
  _globals['_QUERYRAWCONTRACTSTATERESPONSE']._serialized_end=1601
  _globals['_QUERYSMARTCONTRACTSTATEREQUEST']._serialized_start=1604
  _globals['_QUERYSMARTCONTRACTSTATEREQUEST']._serialized_end=1759
  _globals['_QUERYSMARTCONTRACTSTATERESPONSE']._serialized_start=1761
  _globals['_QUERYSMARTCONTRACTSTATERESPONSE']._serialized_end=1854
  _globals['_QUERYCODEREQUEST']._serialized_start=1856
  _globals['_QUERYCODEREQUEST']._serialized_end=1899
  _globals['_CODEINFORESPONSE']._serialized_start=1902
  _globals['_CODEINFORESPONSE']._serialized_end=2214
  _globals['_QUERYCODERESPONSE']._serialized_start=2217
  _globals['_QUERYCODERESPONSE']._serialized_end=2347
  _globals['_QUERYCODESREQUEST']._serialized_start=2349
  _globals['_QUERYCODESREQUEST']._serialized_end=2440
  _globals['_QUERYCODESRESPONSE']._serialized_start=2443
  _globals['_QUERYCODESRESPONSE']._serialized_end=2614
  _globals['_QUERYPINNEDCODESREQUEST']._serialized_start=2616
  _globals['_QUERYPINNEDCODESREQUEST']._serialized_end=2713
  _globals['_QUERYPINNEDCODESRESPONSE']._serialized_start=2716
  _globals['_QUERYPINNEDCODESRESPONSE']._serialized_end=2855
  _globals['_QUERYPARAMSREQUEST']._serialized_start=2857
  _globals['_QUERYPARAMSREQUEST']._serialized_end=2877
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=2879
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=2961
  _globals['_QUERYCONTRACTSBYCREATORREQUEST']._serialized_start=2964
  _globals['_QUERYCONTRACTSBYCREATORREQUEST']._serialized_end=3135
  _globals['_QUERYCONTRACTSBYCREATORRESPONSE']._serialized_start=3138
  _globals['_QUERYCONTRACTSBYCREATORRESPONSE']._serialized_end=3317
  _globals['_QUERYBUILDADDRESSREQUEST']._serialized_start=3320
  _globals['_QUERYBUILDADDRESSREQUEST']._serialized_end=3491
  _globals['_QUERYBUILDADDRESSRESPONSE']._serialized_start=3493
  _globals['_QUERYBUILDADDRESSRESPONSE']._serialized_end=3572
  _globals['_QUERY']._serialized_start=3575
  _globals['_QUERY']._serialized_end=5462
# @@protoc_insertion_point(module_scope)
