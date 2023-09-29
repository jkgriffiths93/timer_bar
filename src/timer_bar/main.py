class TimerBar:
    '''
    '''
    def __init__(self, steps, total_length=50, blank='-', filled='▊', left_border='|', right_border='|', prefix_text='', suffix_text=''):
        self.steps        = steps
        self.total_length = total_length
        self.blank        = blank
        self.filled       = filled
        self.left_border  = left_border
        self.right_border = right_border
        self.prefix_text  = prefix_text
        self.suffix_text  = suffix_text
        self.prebar_len   = len(self.prefix_text+self.left_border)
        self.start_list   = list(self.prefix_text+self.left_border + self.blank*self.total_length + self.right_border+self.suffix_text)
        self.start_text   = ''.join(self.start_list)
        self.current_list = self.start_list.copy()
        self.current_text = self.start_text
    
    def text_at_step(self, step):
        self.current_list = self.start_list.copy()
        adjusted_step = int(min(round((step+1)/self.steps*self.total_length,0), self.total_length))
        for i in range(adjusted_step):
            self.current_list[i+self.prebar_len] = self.filled
        self.current_text = ''.join(self.current_list)
        return self.current_text
    
    def suffix_update(self, string_input):
        self.suffix_text = string_input
        self.start_list = list(self.prefix_text+self.left_border + self.blank*self.total_length + self.right_border+self.suffix_text)
        self.start_text = ''.join(self.start_list)
