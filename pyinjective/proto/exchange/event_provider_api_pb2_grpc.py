# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pyinjective.proto.exchange import event_provider_api_pb2 as exchange_dot_event__provider__api__pb2

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
        + f' but the generated code in exchange/event_provider_api_pb2_grpc.py depends on'
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
        + f' but the generated code in exchange/event_provider_api_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class EventProviderAPIStub(object):
    """EventProviderAPI provides processed block events for different backends.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetLatestHeight = channel.unary_unary(
                '/event_provider_api.EventProviderAPI/GetLatestHeight',
                request_serializer=exchange_dot_event__provider__api__pb2.GetLatestHeightRequest.SerializeToString,
                response_deserializer=exchange_dot_event__provider__api__pb2.GetLatestHeightResponse.FromString,
                _registered_method=True)
        self.StreamBlockEvents = channel.unary_stream(
                '/event_provider_api.EventProviderAPI/StreamBlockEvents',
                request_serializer=exchange_dot_event__provider__api__pb2.StreamBlockEventsRequest.SerializeToString,
                response_deserializer=exchange_dot_event__provider__api__pb2.StreamBlockEventsResponse.FromString,
                _registered_method=True)
        self.GetBlockEventsRPC = channel.unary_unary(
                '/event_provider_api.EventProviderAPI/GetBlockEventsRPC',
                request_serializer=exchange_dot_event__provider__api__pb2.GetBlockEventsRPCRequest.SerializeToString,
                response_deserializer=exchange_dot_event__provider__api__pb2.GetBlockEventsRPCResponse.FromString,
                _registered_method=True)
        self.GetCustomEventsRPC = channel.unary_unary(
                '/event_provider_api.EventProviderAPI/GetCustomEventsRPC',
                request_serializer=exchange_dot_event__provider__api__pb2.GetCustomEventsRPCRequest.SerializeToString,
                response_deserializer=exchange_dot_event__provider__api__pb2.GetCustomEventsRPCResponse.FromString,
                _registered_method=True)
        self.GetABCIBlockEvents = channel.unary_unary(
                '/event_provider_api.EventProviderAPI/GetABCIBlockEvents',
                request_serializer=exchange_dot_event__provider__api__pb2.GetABCIBlockEventsRequest.SerializeToString,
                response_deserializer=exchange_dot_event__provider__api__pb2.GetABCIBlockEventsResponse.FromString,
                _registered_method=True)


class EventProviderAPIServicer(object):
    """EventProviderAPI provides processed block events for different backends.
    """

    def GetLatestHeight(self, request, context):
        """Get latest block from event provider
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamBlockEvents(self, request, context):
        """Stream processed block events for selected backend
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockEventsRPC(self, request, context):
        """Get processed block events for selected backend
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCustomEventsRPC(self, request, context):
        """Get custom processed block events for selected backend
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetABCIBlockEvents(self, request, context):
        """Get raw block events for selected height
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventProviderAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetLatestHeight': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLatestHeight,
                    request_deserializer=exchange_dot_event__provider__api__pb2.GetLatestHeightRequest.FromString,
                    response_serializer=exchange_dot_event__provider__api__pb2.GetLatestHeightResponse.SerializeToString,
            ),
            'StreamBlockEvents': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamBlockEvents,
                    request_deserializer=exchange_dot_event__provider__api__pb2.StreamBlockEventsRequest.FromString,
                    response_serializer=exchange_dot_event__provider__api__pb2.StreamBlockEventsResponse.SerializeToString,
            ),
            'GetBlockEventsRPC': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockEventsRPC,
                    request_deserializer=exchange_dot_event__provider__api__pb2.GetBlockEventsRPCRequest.FromString,
                    response_serializer=exchange_dot_event__provider__api__pb2.GetBlockEventsRPCResponse.SerializeToString,
            ),
            'GetCustomEventsRPC': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCustomEventsRPC,
                    request_deserializer=exchange_dot_event__provider__api__pb2.GetCustomEventsRPCRequest.FromString,
                    response_serializer=exchange_dot_event__provider__api__pb2.GetCustomEventsRPCResponse.SerializeToString,
            ),
            'GetABCIBlockEvents': grpc.unary_unary_rpc_method_handler(
                    servicer.GetABCIBlockEvents,
                    request_deserializer=exchange_dot_event__provider__api__pb2.GetABCIBlockEventsRequest.FromString,
                    response_serializer=exchange_dot_event__provider__api__pb2.GetABCIBlockEventsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'event_provider_api.EventProviderAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('event_provider_api.EventProviderAPI', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class EventProviderAPI(object):
    """EventProviderAPI provides processed block events for different backends.
    """

    @staticmethod
    def GetLatestHeight(request,
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
            '/event_provider_api.EventProviderAPI/GetLatestHeight',
            exchange_dot_event__provider__api__pb2.GetLatestHeightRequest.SerializeToString,
            exchange_dot_event__provider__api__pb2.GetLatestHeightResponse.FromString,
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
    def StreamBlockEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/event_provider_api.EventProviderAPI/StreamBlockEvents',
            exchange_dot_event__provider__api__pb2.StreamBlockEventsRequest.SerializeToString,
            exchange_dot_event__provider__api__pb2.StreamBlockEventsResponse.FromString,
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
    def GetBlockEventsRPC(request,
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
            '/event_provider_api.EventProviderAPI/GetBlockEventsRPC',
            exchange_dot_event__provider__api__pb2.GetBlockEventsRPCRequest.SerializeToString,
            exchange_dot_event__provider__api__pb2.GetBlockEventsRPCResponse.FromString,
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
    def GetCustomEventsRPC(request,
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
            '/event_provider_api.EventProviderAPI/GetCustomEventsRPC',
            exchange_dot_event__provider__api__pb2.GetCustomEventsRPCRequest.SerializeToString,
            exchange_dot_event__provider__api__pb2.GetCustomEventsRPCResponse.FromString,
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
    def GetABCIBlockEvents(request,
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
            '/event_provider_api.EventProviderAPI/GetABCIBlockEvents',
            exchange_dot_event__provider__api__pb2.GetABCIBlockEventsRequest.SerializeToString,
            exchange_dot_event__provider__api__pb2.GetABCIBlockEventsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
