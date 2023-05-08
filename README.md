Aquí tienes el README.md actualizado con una licencia GPL en lugar de la licencia MIT:

```markdown
# Toggle Touchpad/Trackpad for Linux

This Python script allows you to toggle the touchpad/trackpad on your Linux laptop using 'synclient', 'xinput', or 'libinput'.

## Prerequisites

- Python 3.x
- Linux operating system
- Required packages: `xinput`, `libinput`, or `synclient` (depending on your system)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/togglepad.git
   cd togglepad
   ```

2. Install the required dependencies:

   - For 'xinput':

     ```bash
     sudo apt-get install xinput
     ```

   - For 'libinput':

     ```bash
     sudo apt-get install libinput-tools
     ```

   - For 'synclient':

     ```bash
     sudo apt-get install xserver-xorg-input-synaptics
     ```

## Usage

1. Open a terminal and navigate to the project directory.

2. Run the script:

   ```bash
   python togglepad.py
   ```

3. The script will detect the current state of the touchpad/trackpad and provide options to toggle its status.

4. Follow the on-screen instructions to enable or disable the touchpad/trackpad.

## Customization

- You can modify the script to suit your specific needs. For example, you can change the command or add additional functionality.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, feel free to create a pull request.

## License

This project is licensed under the [GPL License](LICENSE).
```

Recuerda que siempre debes asegurarte de entender y cumplir con los términos y condiciones de la licencia que elijas utilizar.
