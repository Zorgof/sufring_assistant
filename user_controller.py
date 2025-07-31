class UserController:
    """Obsługuje wejście i wyjście użytkownika."""
    @staticmethod
    def get_url() -> str:
        print("Hi surfer, provide URL to summarize:")
        return input("Enter URL: ").strip()

    @staticmethod
    def show_message(msg: str):
        print(msg)

    @staticmethod
    def show_summary(summaries):
        if summaries:
            print("\n".join(summaries))
        else:
            print("No summary generated.")