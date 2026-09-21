import unittest

from main import build_message


class BuildMessageTests(unittest.TestCase):
    def test_build_message_mentions_python_and_agents(self) -> None:
        self.assertEqual(
            build_message(),
            "We're writing Python Code with Copilot Agents.",
        )


if __name__ == "__main__":
    unittest.main()
