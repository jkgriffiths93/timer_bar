class TimerBar:
    """
    An object to manage a bar is initially blank and then filled to show progress in a process where both the total number of iterations and the current iteration is known

    -- input attributes --
    steps (integer): total number of iterations in the process
    total_length (integer): total number of characters that the bar will take up (excluding side borders; default: 50)
    blank (string): character used for the blank/to be filled portion of bar (default: '-')
    filled (string): character used for the filled portion of the bar (default: '▊')
    left_border (string): character used for the left border of the bar (default: '|')
    right_border (string): character used for the right border of the bar (default: '|')
    prefix_text (string): text that proceeds the bar (default: '')
    suffix_text (string): text that follows the bar (default: '')
    print_after (boolean): whether the bar will be printed before (False) or after (True) action is taken (default: False)

    -- non-input attributes --
    prebar_len (integer): number of characters before the bar (left_border + prefix_text)
    start_list (list): string list at start of process of each individual character of the bar + additional components (borders, text, etc.)
    start_text (string): text output with a blank bar (before process begins)
    current_list (list): string list at current state of process of each individual character of the bar + additional components (borders, text, etc.)
    current_text (string): text output at current step in process

    -- methods (see method for inputs, etc.) --
    text_at_step: updates timer bar output text for the input step, both updating current_text and returning that value
    update_attribute: updates any attribute of the TimerBar; should be used instead of making direct updates to ensure that dependent variables are updated too
    prefix_update: simplifies update_attribute to update just prefix text
    suffix_update: simplifies update_attribute to update just suffix text
    restart: sets timer bar back to step 0
    """

    def __init__(
        self,
        steps: int,
        total_length: int = 50,
        blank: str = "-",
        filled: str = "▊",
        left_border: str = "|",
        right_border: str = "|",
        prefix_text: str = "",
        suffix_text: str = "",
        print_after: bool = False,
    ):
        self.steps = steps
        self.total_length = total_length
        self.blank = blank
        self.filled = filled
        self.left_border = left_border
        self.right_border = right_border
        self.prefix_text = prefix_text
        self.suffix_text = suffix_text
        self.print_after = print_after
        self.prebar_len = len(self.prefix_text + self.left_border)
        self.start_list = list(
            self.prefix_text
            + self.left_border
            + (self.blank * self.total_length)[: self.total_length]
            + self.right_border
            + self.suffix_text
        )
        self.start_text = "".join(self.start_list)
        self.current_list = self.start_list.copy()
        self.current_text = self.start_text

    def text_at_step(self, step: int) -> str:
        """
        Returns a string of the current timer bar progress

        -- inputs --
        step (int): current step
        """
        self.current_list = self.start_list.copy()
        adjusted_step = int(
            min(
                round(
                    (step + int(self.print_after)) / self.steps * self.total_length, 0
                ),
                self.total_length,
            )
        )
        filled_len = len(self.filled)
        filled_tic = 0
        for i in range(adjusted_step):
            self.current_list[i + self.prebar_len] = self.filled[filled_tic]
            filled_tic = (filled_tic + 1) % filled_len
        self.current_text = "".join(self.current_list)
        return self.current_text

    def update_attribute(
        self,
        steps: int = None,
        total_length: int = None,
        blank: str = None,
        filled: str = None,
        left_border: str = None,
        right_border: str = None,
        prefix_text: str = None,
        suffix_text: str = None,
        print_after: bool = None,
    ):
        """
        Updates needed attributes of the TimerBar object and flows through changes to dependency characteristics

        -- inputs --
        ** All inputs are None by default; exclude characteristics that you do not want changed **
        steps (integer): total number of iterations in the process
        total_length (integer): total number of characters that the bar will take up (excluding side borders)
        blank (string): character used for the blank/to be filled portion of bar
        filled (string): character used for the filled portion of the bar
        left_border (string): character used for the left border of the bar
        right_border (string): character used for the right border of the bar
        prefix_text (string): text that proceeds the bar
        suffix_text (string): text that follows the bar
        print_after (boolean): whether the bar will be printed before (False) or after (True) action is taken
        """
        if steps is not None:
            self.steps = steps
        if total_length is not None:
            self.total_length = total_length
        if blank is not None:
            self.blank = blank
        if filled is not None:
            self.filled = filled
        if left_border is not None:
            self.left_border = left_border
        if right_border is not None:
            self.right_border = right_border
        if prefix_text is not None:
            self.prefix_text = prefix_text
        if suffix_text is not None:
            self.suffix_text = suffix_text
        if print_after is not None:
            self.print_after = print_after

        if (
            self.prefix_text is not None
            or self.left_border is not None
            or self.blank is not None
            or self.total_length is not None
            or self.right_border is not None
            or self.suffix_text is not None
        ):
            if self.prefix_text is not None or self.left_border is not None:
                self.prebar_len = len(self.prefix_text + self.left_border)
            self.start_list = list(
                self.prefix_text
                + self.left_border
                + self.blank * self.total_length
                + self.right_border
                + self.suffix_text
            )
            self.start_text = "".join(self.start_list)
            self.current_list = self.start_list.copy()
            self.current_text = self.start_text

    def prefix_update(self, string_input: str):
        """
        updates the prefix text using update_attribute (simplifies process)

        -- inputs --
        string_input (string): new prefix text
        """
        self.update_attribute(prefix_text=string_input)

    def suffix_update(self, string_input: str):
        """
        updates the suffix text using update_attribute (simplifies process)

        -- inputs --
        string_input (string): new suffix text
        """
        self.update_attribute(suffix_text=string_input)

    def restart(self):
        """
        restarts the TimerBar, setting bar back to step 0
        """
        self.start_list = list(
            self.prefix_text
            + self.left_border
            + (self.blank * self.total_length)[: self.total_length]
            + self.right_border
            + self.suffix_text
        )
        self.start_text = "".join(self.start_list)
        self.current_list = self.start_list.copy()
        self.current_text = self.start_text
