# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pyinjective.proto.exchange import injective_trading_rpc_pb2 as exchange_dot_injective__trading__rpc__pb2

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
        + f' but the generated code in exchange/injective_trading_rpc_pb2_grpc.py depends on'
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
        + f' but the generated code in exchange/injective_trading_rpc_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class InjectiveTradingRPCStub(object):
    """InjectiveTradingStrategiesRPC defined a gRPC service for Injective Trading
    Strategies.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListTradingStrategies = channel.unary_unary(
                '/injective_trading_rpc.InjectiveTradingRPC/ListTradingStrategies',
                request_serializer=exchange_dot_injective__trading__rpc__pb2.ListTradingStrategiesRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__trading__rpc__pb2.ListTradingStrategiesResponse.FromString,
                _registered_method=True)


class InjectiveTradingRPCServicer(object):
    """InjectiveTradingStrategiesRPC defined a gRPC service for Injective Trading
    Strategies.
    """

    def ListTradingStrategies(self, request, context):
        """Lists all trading strategies
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InjectiveTradingRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListTradingStrategies': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTradingStrategies,
                    request_deserializer=exchange_dot_injective__trading__rpc__pb2.ListTradingStrategiesRequest.FromString,
                    response_serializer=exchange_dot_injective__trading__rpc__pb2.ListTradingStrategiesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective_trading_rpc.InjectiveTradingRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('injective_trading_rpc.InjectiveTradingRPC', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class InjectiveTradingRPC(object):
    """InjectiveTradingStrategiesRPC defined a gRPC service for Injective Trading
    Strategies.
    """

    @staticmethod
    def ListTradingStrategies(request,
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
            '/injective_trading_rpc.InjectiveTradingRPC/ListTradingStrategies',
            exchange_dot_injective__trading__rpc__pb2.ListTradingStrategiesRequest.SerializeToString,
            exchange_dot_injective__trading__rpc__pb2.ListTradingStrategiesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
