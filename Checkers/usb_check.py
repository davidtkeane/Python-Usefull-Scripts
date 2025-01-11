import usb.core
import usb.util

# Find all connected USB devices
devices = usb.core.find(find_all=True)

# Iterate over every device
for i, dev in enumerate(devices):
    
    # Print the USB port number
    print(f"USB Port {i}:")
    
    # Print the USB port type
    print(f" USB Port Type: {dev.port_numbers}")
    
    # Initialize default values
    manufacturer = product = serial_number = "Unknown"

    try:
        # Attempt to get USB device details
        manufacturer = usb.util.get_string(dev, 256, dev.iManufacturer)
        product = usb.util.get_string(dev, 256, dev.iProduct)
        serial_number = usb.util.get_string(dev, 256, dev.iSerialNumber)
    except usb.core.USBError as e:
        print(f"An error occurred while getting USB details: {str(e)}")
    
    # Print USB device details
    print(" USB Device Details:")
    print(f"    Manufacturer: {manufacturer}")
    print(f"    Product: {product}")
    print(f"    Serial Number: {serial_number}")
