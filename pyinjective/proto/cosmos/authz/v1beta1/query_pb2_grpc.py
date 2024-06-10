# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pyinjective.proto.cosmos.authz.v1beta1 import query_pb2 as cosmos_dot_authz_dot_v1beta1_dot_query__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in cosmos/authz/v1beta1/query_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in cosmos/authz/v1beta1/query_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Grants = channel.unary_unary(
                '/cosmos.authz.v1beta1.Query/Grants',
                request_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsRequest.SerializeToString,
                response_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsResponse.FromString,
                _registered_method=True)
        self.GranterGrants = channel.unary_unary(
                '/cosmos.authz.v1beta1.Query/GranterGrants',
                request_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranterGrantsRequest.SerializeToString,
                response_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranterGrantsResponse.FromString,
                _registered_method=True)
        self.GranteeGrants = channel.unary_unary(
                '/cosmos.authz.v1beta1.Query/GranteeGrants',
                request_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranteeGrantsRequest.SerializeToString,
                response_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranteeGrantsResponse.FromString,
                _registered_method=True)


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Grants(self, request, context):
        """Returns list of `Authorization`, granted to the grantee by the granter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GranterGrants(self, request, context):
        """GranterGrants returns list of `GrantAuthorization`, granted by granter.

        Since: cosmos-sdk 0.46
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GranteeGrants(self, request, context):
        """GranteeGrants returns a list of `GrantAuthorization` by grantee.

        Since: cosmos-sdk 0.46
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Grants': grpc.unary_unary_rpc_method_handler(
                    servicer.Grants,
                    request_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsRequest.FromString,
                    response_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsResponse.SerializeToString,
            ),
            'GranterGrants': grpc.unary_unary_rpc_method_handler(
                    servicer.GranterGrants,
                    request_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranterGrantsRequest.FromString,
                    response_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranterGrantsResponse.SerializeToString,
            ),
            'GranteeGrants': grpc.unary_unary_rpc_method_handler(
                    servicer.GranteeGrants,
                    request_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranteeGrantsRequest.FromString,
                    response_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranteeGrantsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.authz.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cosmos.authz.v1beta1.Query', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Grants(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cosmos.authz.v1beta1.Query/Grants',
            cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsRequest.SerializeToString,
            cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GranterGrants(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cosmos.authz.v1beta1.Query/GranterGrants',
            cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranterGrantsRequest.SerializeToString,
            cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranterGrantsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GranteeGrants(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cosmos.authz.v1beta1.Query/GranteeGrants',
            cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranteeGrantsRequest.SerializeToString,
            cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGranteeGrantsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
