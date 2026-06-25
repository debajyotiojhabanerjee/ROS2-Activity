#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from activity_service_pkg.srv import ActivityCheck


class ActivityClient(Node):

    SERVICE_NAME = "check_activity"
    TIMEOUT_SEC = 5.0  

    def __init__(self):
        super().__init__("activity_client")

        self._client = self.create_client(ActivityCheck, self.SERVICE_NAME)

    def send_request(self) -> str | None:
        """
        Block until the server is available, send an empty request, and
        return the response message string (or None on timeout/error).
        """
        self.get_logger().info(
            f"[ActivityClient] Waiting for service '/{self.SERVICE_NAME}' …"
        )

        if not self._client.wait_for_service(timeout_sec=self.TIMEOUT_SEC):
            self.get_logger().error(
                f"[ActivityClient] Service not available after "
                f"{self.TIMEOUT_SEC:.0f} s. Is the server running?"
            )
            return None

        request = ActivityCheck.Request()
        self.get_logger().info("[ActivityClient] Sending request …")
        future = self._client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            return future.result().message
        else:
            self.get_logger().error(
                f"[ActivityClient] Service call failed: {future.exception()}"
            )
            return None


def main(args=None):
    rclpy.init(args=args)

    client_node = ActivityClient()

    try:
        reply = client_node.send_request()
        if reply is not None:
            print(f"\n[ActivityClient] Server replied:\n  → {reply}\n")
        else:
            sys.exit(1)
    except KeyboardInterrupt:
        pass
    finally:
        client_node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
