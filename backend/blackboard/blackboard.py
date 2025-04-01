class Blackboard:
    def __init__(self, image_path, post_details):
        self.image_data = image_path
        self.input_data = post_details
        self.output_data = []

    def update_identification(self, identification):
        self.output_data.append(identification)

    def return_identification(self):
        return self.output_data
