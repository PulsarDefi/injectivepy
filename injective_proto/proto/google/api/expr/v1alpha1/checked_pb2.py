from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/expr/v1alpha1/checked.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective_proto.proto.google.api.expr.v1alpha1 import syntax_pb2 as google_dot_api_dot_expr_dot_v1alpha1_dot_syntax__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n&google/api/expr/v1alpha1/checked.proto\x12\x18google.api.expr.v1alpha1\x1a%google/api/expr/v1alpha1/syntax.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x9a\x04\n\x0b\x43heckedExpr\x12\\\n\rreference_map\x18\x02 \x03(\x0b\x32\x37.google.api.expr.v1alpha1.CheckedExpr.ReferenceMapEntryR\x0creferenceMap\x12M\n\x08type_map\x18\x03 \x03(\x0b\x32\x32.google.api.expr.v1alpha1.CheckedExpr.TypeMapEntryR\x07typeMap\x12\x45\n\x0bsource_info\x18\x05 \x01(\x0b\x32$.google.api.expr.v1alpha1.SourceInfoR\nsourceInfo\x12!\n\x0c\x65xpr_version\x18\x06 \x01(\tR\x0b\x65xprVersion\x12\x32\n\x04\x65xpr\x18\x04 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprR\x04\x65xpr\x1a\x64\n\x11ReferenceMapEntry\x12\x10\n\x03key\x18\x01 \x01(\x03R\x03key\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32#.google.api.expr.v1alpha1.ReferenceR\x05value:\x02\x38\x01\x1aZ\n\x0cTypeMapEntry\x12\x10\n\x03key\x18\x01 \x01(\x03R\x03key\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.TypeR\x05value:\x02\x38\x01\"\xc8\x0b\n\x04Type\x12*\n\x03\x64yn\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\x03\x64yn\x12\x30\n\x04null\x18\x02 \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00R\x04null\x12L\n\tprimitive\x18\x03 \x01(\x0e\x32,.google.api.expr.v1alpha1.Type.PrimitiveTypeH\x00R\tprimitive\x12H\n\x07wrapper\x18\x04 \x01(\x0e\x32,.google.api.expr.v1alpha1.Type.PrimitiveTypeH\x00R\x07wrapper\x12M\n\nwell_known\x18\x05 \x01(\x0e\x32,.google.api.expr.v1alpha1.Type.WellKnownTypeH\x00R\twellKnown\x12\x46\n\tlist_type\x18\x06 \x01(\x0b\x32\'.google.api.expr.v1alpha1.Type.ListTypeH\x00R\x08listType\x12\x43\n\x08map_type\x18\x07 \x01(\x0b\x32&.google.api.expr.v1alpha1.Type.MapTypeH\x00R\x07mapType\x12I\n\x08\x66unction\x18\x08 \x01(\x0b\x32+.google.api.expr.v1alpha1.Type.FunctionTypeH\x00R\x08\x66unction\x12#\n\x0cmessage_type\x18\t \x01(\tH\x00R\x0bmessageType\x12\x1f\n\ntype_param\x18\n \x01(\tH\x00R\ttypeParam\x12\x34\n\x04type\x18\x0b \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.TypeH\x00R\x04type\x12.\n\x05\x65rror\x18\x0c \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\x05\x65rror\x12R\n\rabstract_type\x18\x0e \x01(\x0b\x32+.google.api.expr.v1alpha1.Type.AbstractTypeH\x00R\x0c\x61\x62stractType\x1aG\n\x08ListType\x12;\n\telem_type\x18\x01 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.TypeR\x08\x65lemType\x1a\x83\x01\n\x07MapType\x12\x39\n\x08key_type\x18\x01 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.TypeR\x07keyType\x12=\n\nvalue_type\x18\x02 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.TypeR\tvalueType\x1a\x8c\x01\n\x0c\x46unctionType\x12?\n\x0bresult_type\x18\x01 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.TypeR\nresultType\x12;\n\targ_types\x18\x02 \x03(\x0b\x32\x1e.google.api.expr.v1alpha1.TypeR\x08\x61rgTypes\x1ak\n\x0c\x41\x62stractType\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12G\n\x0fparameter_types\x18\x02 \x03(\x0b\x32\x1e.google.api.expr.v1alpha1.TypeR\x0eparameterTypes\"s\n\rPrimitiveType\x12\x1e\n\x1aPRIMITIVE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04\x42OOL\x10\x01\x12\t\n\x05INT64\x10\x02\x12\n\n\x06UINT64\x10\x03\x12\n\n\x06\x44OUBLE\x10\x04\x12\n\n\x06STRING\x10\x05\x12\t\n\x05\x42YTES\x10\x06\"V\n\rWellKnownType\x12\x1f\n\x1bWELL_KNOWN_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03\x41NY\x10\x01\x12\r\n\tTIMESTAMP\x10\x02\x12\x0c\n\x08\x44URATION\x10\x03\x42\x0b\n\ttype_kind\"\xb3\x05\n\x04\x44\x65\x63l\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12@\n\x05ident\x18\x02 \x01(\x0b\x32(.google.api.expr.v1alpha1.Decl.IdentDeclH\x00R\x05ident\x12I\n\x08\x66unction\x18\x03 \x01(\x0b\x32+.google.api.expr.v1alpha1.Decl.FunctionDeclH\x00R\x08\x66unction\x1a\x8b\x01\n\tIdentDecl\x12\x32\n\x04type\x18\x01 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.TypeR\x04type\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32\".google.api.expr.v1alpha1.ConstantR\x05value\x12\x10\n\x03\x64oc\x18\x03 \x01(\tR\x03\x64oc\x1a\xee\x02\n\x0c\x46unctionDecl\x12R\n\toverloads\x18\x01 \x03(\x0b\x32\x34.google.api.expr.v1alpha1.Decl.FunctionDecl.OverloadR\toverloads\x1a\x89\x02\n\x08Overload\x12\x1f\n\x0boverload_id\x18\x01 \x01(\tR\noverloadId\x12\x36\n\x06params\x18\x02 \x03(\x0b\x32\x1e.google.api.expr.v1alpha1.TypeR\x06params\x12\x1f\n\x0btype_params\x18\x03 \x03(\tR\ntypeParams\x12?\n\x0bresult_type\x18\x04 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.TypeR\nresultType\x12\x30\n\x14is_instance_function\x18\x05 \x01(\x08R\x12isInstanceFunction\x12\x10\n\x03\x64oc\x18\x06 \x01(\tR\x03\x64ocB\x0b\n\tdecl_kind\"z\n\tReference\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1f\n\x0boverload_id\x18\x03 \x03(\tR\noverloadId\x12\x38\n\x05value\x18\x04 \x01(\x0b\x32\".google.api.expr.v1alpha1.ConstantR\x05valueB\xf0\x01\n\x1c\x63om.google.api.expr.v1alpha1B\x0c\x43heckedProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01\xa2\x02\x03GAE\xaa\x02\x18Google.Api.Expr.V1alpha1\xca\x02\x18Google\\Api\\Expr\\V1alpha1\xe2\x02$Google\\Api\\Expr\\V1alpha1\\GPBMetadata\xea\x02\x1bGoogle::Api::Expr::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.expr.v1alpha1.checked_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.google.api.expr.v1alpha1B\014CheckedProtoP\001Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\370\001\001\242\002\003GAE\252\002\030Google.Api.Expr.V1alpha1\312\002\030Google\\Api\\Expr\\V1alpha1\342\002$Google\\Api\\Expr\\V1alpha1\\GPBMetadata\352\002\033Google::Api::Expr::V1alpha1'
  _globals['_CHECKEDEXPR_REFERENCEMAPENTRY']._loaded_options = None
  _globals['_CHECKEDEXPR_REFERENCEMAPENTRY']._serialized_options = b'8\001'
  _globals['_CHECKEDEXPR_TYPEMAPENTRY']._loaded_options = None
  _globals['_CHECKEDEXPR_TYPEMAPENTRY']._serialized_options = b'8\001'
  _globals['_CHECKEDEXPR']._serialized_start=167
  _globals['_CHECKEDEXPR']._serialized_end=705
  _globals['_CHECKEDEXPR_REFERENCEMAPENTRY']._serialized_start=513
  _globals['_CHECKEDEXPR_REFERENCEMAPENTRY']._serialized_end=613
  _globals['_CHECKEDEXPR_TYPEMAPENTRY']._serialized_start=615
  _globals['_CHECKEDEXPR_TYPEMAPENTRY']._serialized_end=705
  _globals['_TYPE']._serialized_start=708
  _globals['_TYPE']._serialized_end=2188
  _globals['_TYPE_LISTTYPE']._serialized_start=1513
  _globals['_TYPE_LISTTYPE']._serialized_end=1584
  _globals['_TYPE_MAPTYPE']._serialized_start=1587
  _globals['_TYPE_MAPTYPE']._serialized_end=1718
  _globals['_TYPE_FUNCTIONTYPE']._serialized_start=1721
  _globals['_TYPE_FUNCTIONTYPE']._serialized_end=1861
  _globals['_TYPE_ABSTRACTTYPE']._serialized_start=1863
  _globals['_TYPE_ABSTRACTTYPE']._serialized_end=1970
  _globals['_TYPE_PRIMITIVETYPE']._serialized_start=1972
  _globals['_TYPE_PRIMITIVETYPE']._serialized_end=2087
  _globals['_TYPE_WELLKNOWNTYPE']._serialized_start=2089
  _globals['_TYPE_WELLKNOWNTYPE']._serialized_end=2175
  _globals['_DECL']._serialized_start=2191
  _globals['_DECL']._serialized_end=2882
  _globals['_DECL_IDENTDECL']._serialized_start=2361
  _globals['_DECL_IDENTDECL']._serialized_end=2500
  _globals['_DECL_FUNCTIONDECL']._serialized_start=2503
  _globals['_DECL_FUNCTIONDECL']._serialized_end=2869
  _globals['_DECL_FUNCTIONDECL_OVERLOAD']._serialized_start=2604
  _globals['_DECL_FUNCTIONDECL_OVERLOAD']._serialized_end=2869
  _globals['_REFERENCE']._serialized_start=2884
  _globals['_REFERENCE']._serialized_end=3006
# @@protoc_insertion_point(module_scope)