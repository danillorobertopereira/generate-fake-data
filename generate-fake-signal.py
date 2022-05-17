import numpy as np

class GenerateFakeSignal:
    
    ___input_signals = None
    ___output_signal = None
    ___qtd_input_signals = None

    def __init__(self, input_signals=None) -> None:
        """__init__

        Args:
            input_signals ([type], optional): The initial input_signal to be deformed. Defaults to None.
        """
        self.___input_signals = input_signals
        self.___output_signal = None
        self.___qtd_input_signals = len(input_signals)
        return 

    def get_input_signals(self, input_signals:list) -> None:
        """AI is creating summary for get_input_signals

        Args:
            input_signals (list): [description]
        """
        self.___input_signals = input_signals
        self.___qtd_input_signals = len(input_signals)
        return

    def generate_noise_input_signal(self, noise_info:dict, position:int=0) -> None:
        """AI is creating summary for generate_noise_input_signal

        Args:
            noise_info (dict): [description]
            position (int, optional): [description]. Defaults to None.
            inplace (bool, optional): [description]. Defaults to True.
        """
        if noise_info['type'] == "identity":
            self.___output_signal = self.___input_signals[position]
        elif noise_info['type'] == "sum_random":            
            noise_values = np.random.random(len(self.___input_signals[position])) * noise_info['param']
            if self.___output_signal is None: 
                self.___output_signal = self.___input_signals[position]
            self.___output_signal = self.___output_signal + noise_values


    def return_output_signal(self) -> list:
        """Return the current output_signal

        Returns:
            list: Current output_signal 
        """
        return self.___output_signal


test = GenerateFakeSignal(input_signals=[[1, 2, 3, 4, 5]])
test.get_input_signals(input_signals=[[1, 2, 3, 4, 5],[5,4,3,2,-1]])
test.generate_noise_input_signal(noise_info={'type':'sum_random', 'param':5})
print(test.return_output_signal())

