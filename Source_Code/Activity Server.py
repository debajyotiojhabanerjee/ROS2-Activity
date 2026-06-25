#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from activity_service_pkg.srv import ActivityCheck


class ActivityServer(Node):
    """Node that counts and responds to ActivityCheck service requests."""

    SERVICE_NAME = "check_activity"

    def __init__(self):
        super().__init__("activity_server")

        
        self._call_count: int = 0

        
        self._srv = self.create_service(
            ActivityCheck,
            self.SERVICE_NAME,
            self._handle_request,
        )

        self.get_logger().info(
            f"[ActivityServer] Ready — listening on '/{self.SERVICE_NAME}'"
        )

  
    def _handle_request(
        self,
        request: ActivityCheck.Request,
        response: ActivityCheck.Response,
    ) -> ActivityCheck.Response:
        """Called every time a client triggers the service."""

        self._call_count += 1

        # Terminal output visible to whoever is running the server
        self.get_logger().info(
            f"[ActivityServer] Service triggered! "
            f"Total calls so far: {self._call_count}"
        )

        # Build the response string
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
        node.get_logger().info("[ActivityServer] Shutting down (Ctrl+C).")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()