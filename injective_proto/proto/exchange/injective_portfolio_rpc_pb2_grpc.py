# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from injective_proto.proto.exchange import injective_portfolio_rpc_pb2 as exchange_dot_injective__portfolio__rpc__pb2


class InjectivePortfolioRPCStub(object):
    """InjectivePortfolioRPC defines gRPC API of Exchange Portfolio provider.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TokenHolders = channel.unary_unary(
                '/injective_portfolio_rpc.InjectivePortfolioRPC/TokenHolders',
                request_serializer=exchange_dot_injective__portfolio__rpc__pb2.TokenHoldersRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__portfolio__rpc__pb2.TokenHoldersResponse.FromString,
                _registered_method=True)
        self.AccountPortfolio = channel.unary_unary(
                '/injective_portfolio_rpc.InjectivePortfolioRPC/AccountPortfolio',
                request_serializer=exchange_dot_injective__portfolio__rpc__pb2.AccountPortfolioRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__portfolio__rpc__pb2.AccountPortfolioResponse.FromString,
                _registered_method=True)
        self.AccountPortfolioBalances = channel.unary_unary(
                '/injective_portfolio_rpc.InjectivePortfolioRPC/AccountPortfolioBalances',
                request_serializer=exchange_dot_injective__portfolio__rpc__pb2.AccountPortfolioBalancesRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__portfolio__rpc__pb2.AccountPortfolioBalancesResponse.FromString,
                _registered_method=True)
        self.StreamAccountPortfolio = channel.unary_stream(
                '/injective_portfolio_rpc.InjectivePortfolioRPC/StreamAccountPortfolio',
                request_serializer=exchange_dot_injective__portfolio__rpc__pb2.StreamAccountPortfolioRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__portfolio__rpc__pb2.StreamAccountPortfolioResponse.FromString,
                _registered_method=True)


class InjectivePortfolioRPCServicer(object):
    """InjectivePortfolioRPC defines gRPC API of Exchange Portfolio provider.
    """

    def TokenHolders(self, request, context):
        """Provide a list of addresses holding a specific token
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountPortfolio(self, request, context):
        """Provide the account's portfolio
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccountPortfolioBalances(self, request, context):
        """Provide the account's portfolio balances
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamAccountPortfolio(self, request, context):
        """Stream the account's portfolio
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InjectivePortfolioRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TokenHolders': grpc.unary_unary_rpc_method_handler(
                    servicer.TokenHolders,
                    request_deserializer=exchange_dot_injective__portfolio__rpc__pb2.TokenHoldersRequest.FromString,
                    response_serializer=exchange_dot_injective__portfolio__rpc__pb2.TokenHoldersResponse.SerializeToString,
            ),
            'AccountPortfolio': grpc.unary_unary_rpc_method_handler(
                    servicer.AccountPortfolio,
                    request_deserializer=exchange_dot_injective__portfolio__rpc__pb2.AccountPortfolioRequest.FromString,
                    response_serializer=exchange_dot_injective__portfolio__rpc__pb2.AccountPortfolioResponse.SerializeToString,
            ),
            'AccountPortfolioBalances': grpc.unary_unary_rpc_method_handler(
                    servicer.AccountPortfolioBalances,
                    request_deserializer=exchange_dot_injective__portfolio__rpc__pb2.AccountPortfolioBalancesRequest.FromString,
                    response_serializer=exchange_dot_injective__portfolio__rpc__pb2.AccountPortfolioBalancesResponse.SerializeToString,
            ),
            'StreamAccountPortfolio': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamAccountPortfolio,
                    request_deserializer=exchange_dot_injective__portfolio__rpc__pb2.StreamAccountPortfolioRequest.FromString,
                    response_serializer=exchange_dot_injective__portfolio__rpc__pb2.StreamAccountPortfolioResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective_portfolio_rpc.InjectivePortfolioRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('injective_portfolio_rpc.InjectivePortfolioRPC', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class InjectivePortfolioRPC(object):
    """InjectivePortfolioRPC defines gRPC API of Exchange Portfolio provider.
    """

    @staticmethod
    def TokenHolders(request,
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
            '/injective_portfolio_rpc.InjectivePortfolioRPC/TokenHolders',
            exchange_dot_injective__portfolio__rpc__pb2.TokenHoldersRequest.SerializeToString,
            exchange_dot_injective__portfolio__rpc__pb2.TokenHoldersResponse.FromString,
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
    def AccountPortfolio(request,
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
            '/injective_portfolio_rpc.InjectivePortfolioRPC/AccountPortfolio',
            exchange_dot_injective__portfolio__rpc__pb2.AccountPortfolioRequest.SerializeToString,
            exchange_dot_injective__portfolio__rpc__pb2.AccountPortfolioResponse.FromString,
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
    def AccountPortfolioBalances(request,
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
            '/injective_portfolio_rpc.InjectivePortfolioRPC/AccountPortfolioBalances',
            exchange_dot_injective__portfolio__rpc__pb2.AccountPortfolioBalancesRequest.SerializeToString,
            exchange_dot_injective__portfolio__rpc__pb2.AccountPortfolioBalancesResponse.FromString,
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
    def StreamAccountPortfolio(request,
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
            '/injective_portfolio_rpc.InjectivePortfolioRPC/StreamAccountPortfolio',
            exchange_dot_injective__portfolio__rpc__pb2.StreamAccountPortfolioRequest.SerializeToString,
            exchange_dot_injective__portfolio__rpc__pb2.StreamAccountPortfolioResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)