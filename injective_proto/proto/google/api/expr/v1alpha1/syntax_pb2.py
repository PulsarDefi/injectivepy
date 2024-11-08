from injective_proto.proto.descriptor import INJECTIVE_DESCRIPTOR_POOL
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/expr/v1alpha1/syntax.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = INJECTIVE_DESCRIPTOR_POOL.AddSerializedFile(b'\n%google/api/expr/v1alpha1/syntax.proto\x12\x18google.api.expr.v1alpha1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x87\x01\n\nParsedExpr\x12\x32\n\x04\x65xpr\x18\x02 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprR\x04\x65xpr\x12\x45\n\x0bsource_info\x18\x03 \x01(\x0b\x32$.google.api.expr.v1alpha1.SourceInfoR\nsourceInfo\"\xcb\r\n\x04\x45xpr\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\x12\x43\n\nconst_expr\x18\x03 \x01(\x0b\x32\".google.api.expr.v1alpha1.ConstantH\x00R\tconstExpr\x12\x45\n\nident_expr\x18\x04 \x01(\x0b\x32$.google.api.expr.v1alpha1.Expr.IdentH\x00R\tidentExpr\x12H\n\x0bselect_expr\x18\x05 \x01(\x0b\x32%.google.api.expr.v1alpha1.Expr.SelectH\x00R\nselectExpr\x12\x42\n\tcall_expr\x18\x06 \x01(\x0b\x32#.google.api.expr.v1alpha1.Expr.CallH\x00R\x08\x63\x61llExpr\x12H\n\tlist_expr\x18\x07 \x01(\x0b\x32).google.api.expr.v1alpha1.Expr.CreateListH\x00R\x08listExpr\x12N\n\x0bstruct_expr\x18\x08 \x01(\x0b\x32+.google.api.expr.v1alpha1.Expr.CreateStructH\x00R\nstructExpr\x12]\n\x12\x63omprehension_expr\x18\t \x01(\x0b\x32,.google.api.expr.v1alpha1.Expr.ComprehensionH\x00R\x11\x63omprehensionExpr\x1a\x1b\n\x05Ident\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x1au\n\x06Select\x12\x38\n\x07operand\x18\x01 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprR\x07operand\x12\x14\n\x05\x66ield\x18\x02 \x01(\tR\x05\x66ield\x12\x1b\n\ttest_only\x18\x03 \x01(\x08R\x08testOnly\x1a\x8e\x01\n\x04\x43\x61ll\x12\x36\n\x06target\x18\x01 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprR\x06target\x12\x1a\n\x08\x66unction\x18\x02 \x01(\tR\x08\x66unction\x12\x32\n\x04\x61rgs\x18\x03 \x03(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprR\x04\x61rgs\x1as\n\nCreateList\x12:\n\x08\x65lements\x18\x01 \x03(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprR\x08\x65lements\x12)\n\x10optional_indices\x18\x02 \x03(\x05R\x0foptionalIndices\x1a\xdb\x02\n\x0c\x43reateStruct\x12!\n\x0cmessage_name\x18\x01 \x01(\tR\x0bmessageName\x12K\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x31.google.api.expr.v1alpha1.Expr.CreateStruct.EntryR\x07\x65ntries\x1a\xda\x01\n\x05\x45ntry\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1d\n\tfield_key\x18\x02 \x01(\tH\x00R\x08\x66ieldKey\x12\x39\n\x07map_key\x18\x03 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprH\x00R\x06mapKey\x12\x34\n\x05value\x18\x04 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprR\x05value\x12%\n\x0eoptional_entry\x18\x05 \x01(\x08R\roptionalEntryB\n\n\x08key_kind\x1a\x9a\x03\n\rComprehension\x12\x19\n\x08iter_var\x18\x01 \x01(\tR\x07iterVar\x12\x1b\n\titer_var2\x18\x08 \x01(\tR\x08iterVar2\x12=\n\niter_range\x18\x02 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprR\titerRange\x12\x19\n\x08\x61\x63\x63u_var\x18\x03 \x01(\tR\x07\x61\x63\x63uVar\x12;\n\taccu_init\x18\x04 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprR\x08\x61\x63\x63uInit\x12\x45\n\x0eloop_condition\x18\x05 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprR\rloopCondition\x12;\n\tloop_step\x18\x06 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprR\x08loopStep\x12\x36\n\x06result\x18\x07 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprR\x06resultB\x0b\n\texpr_kind\"\xc1\x03\n\x08\x43onstant\x12;\n\nnull_value\x18\x01 \x01(\x0e\x32\x1a.google.protobuf.NullValueH\x00R\tnullValue\x12\x1f\n\nbool_value\x18\x02 \x01(\x08H\x00R\tboolValue\x12!\n\x0bint64_value\x18\x03 \x01(\x03H\x00R\nint64Value\x12#\n\x0cuint64_value\x18\x04 \x01(\x04H\x00R\x0buint64Value\x12#\n\x0c\x64ouble_value\x18\x05 \x01(\x01H\x00R\x0b\x64oubleValue\x12#\n\x0cstring_value\x18\x06 \x01(\tH\x00R\x0bstringValue\x12!\n\x0b\x62ytes_value\x18\x07 \x01(\x0cH\x00R\nbytesValue\x12\x46\n\x0e\x64uration_value\x18\x08 \x01(\x0b\x32\x19.google.protobuf.DurationB\x02\x18\x01H\x00R\rdurationValue\x12I\n\x0ftimestamp_value\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01H\x00R\x0etimestampValueB\x0f\n\rconstant_kind\"\x8c\x07\n\nSourceInfo\x12%\n\x0esyntax_version\x18\x01 \x01(\tR\rsyntaxVersion\x12\x1a\n\x08location\x18\x02 \x01(\tR\x08location\x12!\n\x0cline_offsets\x18\x03 \x03(\x05R\x0blineOffsets\x12Q\n\tpositions\x18\x04 \x03(\x0b\x32\x33.google.api.expr.v1alpha1.SourceInfo.PositionsEntryR\tpositions\x12U\n\x0bmacro_calls\x18\x05 \x03(\x0b\x32\x34.google.api.expr.v1alpha1.SourceInfo.MacroCallsEntryR\nmacroCalls\x12N\n\nextensions\x18\x06 \x03(\x0b\x32..google.api.expr.v1alpha1.SourceInfo.ExtensionR\nextensions\x1a\x80\x03\n\tExtension\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12i\n\x13\x61\x66\x66\x65\x63ted_components\x18\x02 \x03(\x0e\x32\x38.google.api.expr.v1alpha1.SourceInfo.Extension.ComponentR\x12\x61\x66\x66\x65\x63tedComponents\x12P\n\x07version\x18\x03 \x01(\x0b\x32\x36.google.api.expr.v1alpha1.SourceInfo.Extension.VersionR\x07version\x1a\x35\n\x07Version\x12\x14\n\x05major\x18\x01 \x01(\x03R\x05major\x12\x14\n\x05minor\x18\x02 \x01(\x03R\x05minor\"o\n\tComponent\x12\x19\n\x15\x43OMPONENT_UNSPECIFIED\x10\x00\x12\x14\n\x10\x43OMPONENT_PARSER\x10\x01\x12\x1a\n\x16\x43OMPONENT_TYPE_CHECKER\x10\x02\x12\x15\n\x11\x43OMPONENT_RUNTIME\x10\x03\x1a<\n\x0ePositionsEntry\x12\x10\n\x03key\x18\x01 \x01(\x03R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x05R\x05value:\x02\x38\x01\x1a]\n\x0fMacroCallsEntry\x12\x10\n\x03key\x18\x01 \x01(\x03R\x03key\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32\x1e.google.api.expr.v1alpha1.ExprR\x05value:\x02\x38\x01\"p\n\x0eSourcePosition\x12\x1a\n\x08location\x18\x01 \x01(\tR\x08location\x12\x16\n\x06offset\x18\x02 \x01(\x05R\x06offset\x12\x12\n\x04line\x18\x03 \x01(\x05R\x04line\x12\x16\n\x06\x63olumn\x18\x04 \x01(\x05R\x06\x63olumnB\xef\x01\n\x1c\x63om.google.api.expr.v1alpha1B\x0bSyntaxProtoP\x01Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\xf8\x01\x01\xa2\x02\x03GAE\xaa\x02\x18Google.Api.Expr.V1alpha1\xca\x02\x18Google\\Api\\Expr\\V1alpha1\xe2\x02$Google\\Api\\Expr\\V1alpha1\\GPBMetadata\xea\x02\x1bGoogle::Api::Expr::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.expr.v1alpha1.syntax_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.google.api.expr.v1alpha1B\013SyntaxProtoP\001Z<google.golang.org/genproto/googleapis/api/expr/v1alpha1;expr\370\001\001\242\002\003GAE\252\002\030Google.Api.Expr.V1alpha1\312\002\030Google\\Api\\Expr\\V1alpha1\342\002$Google\\Api\\Expr\\V1alpha1\\GPBMetadata\352\002\033Google::Api::Expr::V1alpha1'
  _globals['_CONSTANT'].fields_by_name['duration_value']._loaded_options = None
  _globals['_CONSTANT'].fields_by_name['duration_value']._serialized_options = b'\030\001'
  _globals['_CONSTANT'].fields_by_name['timestamp_value']._loaded_options = None
  _globals['_CONSTANT'].fields_by_name['timestamp_value']._serialized_options = b'\030\001'
  _globals['_SOURCEINFO_POSITIONSENTRY']._loaded_options = None
  _globals['_SOURCEINFO_POSITIONSENTRY']._serialized_options = b'8\001'
  _globals['_SOURCEINFO_MACROCALLSENTRY']._loaded_options = None
  _globals['_SOURCEINFO_MACROCALLSENTRY']._serialized_options = b'8\001'
  _globals['_PARSEDEXPR']._serialized_start=163
  _globals['_PARSEDEXPR']._serialized_end=298
  _globals['_EXPR']._serialized_start=301
  _globals['_EXPR']._serialized_end=2040
  _globals['_EXPR_IDENT']._serialized_start=856
  _globals['_EXPR_IDENT']._serialized_end=883
  _globals['_EXPR_SELECT']._serialized_start=885
  _globals['_EXPR_SELECT']._serialized_end=1002
  _globals['_EXPR_CALL']._serialized_start=1005
  _globals['_EXPR_CALL']._serialized_end=1147
  _globals['_EXPR_CREATELIST']._serialized_start=1149
  _globals['_EXPR_CREATELIST']._serialized_end=1264
  _globals['_EXPR_CREATESTRUCT']._serialized_start=1267
  _globals['_EXPR_CREATESTRUCT']._serialized_end=1614
  _globals['_EXPR_CREATESTRUCT_ENTRY']._serialized_start=1396
  _globals['_EXPR_CREATESTRUCT_ENTRY']._serialized_end=1614
  _globals['_EXPR_COMPREHENSION']._serialized_start=1617
  _globals['_EXPR_COMPREHENSION']._serialized_end=2027
  _globals['_CONSTANT']._serialized_start=2043
  _globals['_CONSTANT']._serialized_end=2492
  _globals['_SOURCEINFO']._serialized_start=2495
  _globals['_SOURCEINFO']._serialized_end=3403
  _globals['_SOURCEINFO_EXTENSION']._serialized_start=2862
  _globals['_SOURCEINFO_EXTENSION']._serialized_end=3246
  _globals['_SOURCEINFO_EXTENSION_VERSION']._serialized_start=3080
  _globals['_SOURCEINFO_EXTENSION_VERSION']._serialized_end=3133
  _globals['_SOURCEINFO_EXTENSION_COMPONENT']._serialized_start=3135
  _globals['_SOURCEINFO_EXTENSION_COMPONENT']._serialized_end=3246
  _globals['_SOURCEINFO_POSITIONSENTRY']._serialized_start=3248
  _globals['_SOURCEINFO_POSITIONSENTRY']._serialized_end=3308
  _globals['_SOURCEINFO_MACROCALLSENTRY']._serialized_start=3310
  _globals['_SOURCEINFO_MACROCALLSENTRY']._serialized_end=3403
  _globals['_SOURCEPOSITION']._serialized_start=3405
  _globals['_SOURCEPOSITION']._serialized_end=3517
# @@protoc_insertion_point(module_scope)
