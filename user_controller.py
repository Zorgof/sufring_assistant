"""Controller for user interactions in the Surfer Assistant application."""

class UserController:
    """ Handles user interactions for the Surfer Assistant application. """
    @staticmethod
    def get_url() -> str:
        """Prompts the user for a URL to summarize.
        Returns:
            str: The URL input by the user.
        """
        print("Hi surfer, provide URL to summarize:")
        return input("Enter URL: ").strip()

    @staticmethod
    def show_message(msg: str):
        """Displays a message to the user.
        Args:
            msg (str): The message to display.
        """
        print(msg)

    @staticmethod
    def show_summary(summaries):
        """Displays the summary to the user.
        Args:
            summaries (list): List of summary strings.
        """
        if summaries:
            print("\n".join(summaries))
        else:
            print("No summary generated.")