# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import balance_pb2 as balance__pb2

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
        + f' but the generated code in balance_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class BalanceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBalance = channel.unary_unary(
                '/BalanceService/GetBalance',
                request_serializer=balance__pb2.BalanceRequest.SerializeToString,
                response_deserializer=balance__pb2.BalanceResponse.FromString,
                _registered_method=True)
        self.UpdateBalance = channel.unary_unary(
                '/BalanceService/UpdateBalance',
                request_serializer=balance__pb2.UpdateBalanceRequest.SerializeToString,
                response_deserializer=balance__pb2.UpdateBalanceResponse.FromString,
                _registered_method=True)


class BalanceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBalance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBalance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BalanceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBalance,
                    request_deserializer=balance__pb2.BalanceRequest.FromString,
                    response_serializer=balance__pb2.BalanceResponse.SerializeToString,
            ),
            'UpdateBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBalance,
                    request_deserializer=balance__pb2.UpdateBalanceRequest.FromString,
                    response_serializer=balance__pb2.UpdateBalanceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BalanceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('BalanceService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BalanceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBalance(request,
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
            '/BalanceService/GetBalance',
            balance__pb2.BalanceRequest.SerializeToString,
            balance__pb2.BalanceResponse.FromString,
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
    def UpdateBalance(request,
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
            '/BalanceService/UpdateBalance',
            balance__pb2.UpdateBalanceRequest.SerializeToString,
            balance__pb2.UpdateBalanceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
