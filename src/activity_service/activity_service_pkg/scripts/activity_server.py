#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from activity_service_pkg.srv import ActivityCheck

class ActivityServer(Node):
    def __init__(self):
        super().__init__("activity_server")
        self._call_count = 0
        self._srv = self.create_service(ActivityCheck, "check_activity", self._handle_request)
        self.get_logger().info("[ActivityServer] Ready — listening on '/check_activity'")

    def _handle_request(self, request, response):
        self._call_count += 1
        self.get_logger().info(f"[ActivityServer] Service triggered! Total calls so far: {self._call_count}")
        response.message = (
            f"Your service is currently active and has been called for "
            f"{self._call_count} time{'s' if self._call_count != 1 else ''}."
        )
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ActivityServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("[ActivityServer] Shutting down.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
