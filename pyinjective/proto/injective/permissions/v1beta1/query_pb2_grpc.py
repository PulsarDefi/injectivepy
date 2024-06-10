# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pyinjective.proto.injective.permissions.v1beta1 import query_pb2 as injective_dot_permissions_dot_v1beta1_dot_query__pb2

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
        + f' but the generated code in injective/permissions/v1beta1/query_pb2_grpc.py depends on'
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
        + f' but the generated code in injective/permissions/v1beta1/query_pb2_grpc.py depends on'
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
        self.Params = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/Params',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
                _registered_method=True)
        self.AllNamespaces = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/AllNamespaces',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAllNamespacesRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAllNamespacesResponse.FromString,
                _registered_method=True)
        self.NamespaceByDenom = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/NamespaceByDenom',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceByDenomRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceByDenomResponse.FromString,
                _registered_method=True)
        self.AddressRoles = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/AddressRoles',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAddressRolesRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAddressRolesResponse.FromString,
                _registered_method=True)
        self.AddressesByRole = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/AddressesByRole',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAddressesByRoleRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAddressesByRoleResponse.FromString,
                _registered_method=True)
        self.VouchersForAddress = channel.unary_unary(
                '/injective.permissions.v1beta1.Query/VouchersForAddress',
                request_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVouchersForAddressRequest.SerializeToString,
                response_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVouchersForAddressResponse.FromString,
                _registered_method=True)


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Params(self, request, context):
        """Params defines a gRPC query method that returns the permissions module's
        parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllNamespaces(self, request, context):
        """AllNamespaces defines a gRPC query method that returns the permissions
        module's created namespaces.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NamespaceByDenom(self, request, context):
        """NamespaceByDenom defines a gRPC query method that returns the permissions
        module's namespace associated with the provided denom.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddressRoles(self, request, context):
        """AddressRoles defines a gRPC query method that returns address roles in the
        namespace
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddressesByRole(self, request, context):
        """AddressesByRole defines a gRPC query method that returns a namespace's
        roles associated with the provided address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VouchersForAddress(self, request, context):
        """VouchersForAddress defines a gRPC query method that returns a map of
        vouchers that are held by permissions module for this address, keyed by the
        originator address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
            'AllNamespaces': grpc.unary_unary_rpc_method_handler(
                    servicer.AllNamespaces,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAllNamespacesRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAllNamespacesResponse.SerializeToString,
            ),
            'NamespaceByDenom': grpc.unary_unary_rpc_method_handler(
                    servicer.NamespaceByDenom,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceByDenomRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceByDenomResponse.SerializeToString,
            ),
            'AddressRoles': grpc.unary_unary_rpc_method_handler(
                    servicer.AddressRoles,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAddressRolesRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAddressRolesResponse.SerializeToString,
            ),
            'AddressesByRole': grpc.unary_unary_rpc_method_handler(
                    servicer.AddressesByRole,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAddressesByRoleRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAddressesByRoleResponse.SerializeToString,
            ),
            'VouchersForAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.VouchersForAddress,
                    request_deserializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVouchersForAddressRequest.FromString,
                    response_serializer=injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVouchersForAddressResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.permissions.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('injective.permissions.v1beta1.Query', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Params(request,
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
            '/injective.permissions.v1beta1.Query/Params',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
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
    def AllNamespaces(request,
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
            '/injective.permissions.v1beta1.Query/AllNamespaces',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAllNamespacesRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAllNamespacesResponse.FromString,
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
    def NamespaceByDenom(request,
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
            '/injective.permissions.v1beta1.Query/NamespaceByDenom',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceByDenomRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryNamespaceByDenomResponse.FromString,
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
    def AddressRoles(request,
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
            '/injective.permissions.v1beta1.Query/AddressRoles',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAddressRolesRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAddressRolesResponse.FromString,
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
    def AddressesByRole(request,
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
            '/injective.permissions.v1beta1.Query/AddressesByRole',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAddressesByRoleRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryAddressesByRoleResponse.FromString,
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
    def VouchersForAddress(request,
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
            '/injective.permissions.v1beta1.Query/VouchersForAddress',
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVouchersForAddressRequest.SerializeToString,
            injective_dot_permissions_dot_v1beta1_dot_query__pb2.QueryVouchersForAddressResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
