#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from activity_service_pkg.srv import ActivityCheck

class ActivityClient(Node):
    def __init__(self):
        super().__init__("activity_client")
        self._client = self.create_client(ActivityCheck, "check_activity")

    def send_request(self):
        self.get_logger().info("[ActivityClient] Waiting for service...")
        if not self._client.wait_for_service(timeout_sec=5.0):
            self.get_logger().error("[ActivityClient] Service not available!")
            return None
        future = self._client.call_async(ActivityCheck.Request())
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            return future.result().message
        return None

def main(args=None):
    rclpy.init(args=args)
    node = ActivityClient()
    try:
        reply = node.send_request()
        if reply:
            print(f"\n[ActivityClient] Server replied:\n  → {reply}\n")
        else:
            sys.exit(1)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
