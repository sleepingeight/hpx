import sys
import os

def analyze(log_file):
    if not os.path.exists(log_file):
        print(f"Log file {log_file} not found.")
        return

    try:
        with open(log_file, 'r') as f:
            lines = f.readlines()

        if len(lines) <= 1:
            print("No data collected in RAM profile.")
            return

        used_data = []
        avail_data = []
        for line in lines[1:]:
            parts = line.strip().split(',')
            if len(parts) == 3:
                try:
                    used_data.append(int(parts[1]))
                    avail_data.append(int(parts[2]))
                except ValueError:
                    continue

        if not used_data:
            print("No valid data collected in RAM profile.")
            return

        print(f"\n--- RAM Profiling Results ({log_file}) ---")
        print(f"Peak RAM Used:      {max(used_data)} MB")
        print(f"Minimum RAM Used:   {min(used_data)} MB")
        print(f"Average RAM Used:   {sum(used_data)/len(used_data):.2f} MB")
        print(f"------------------------------------------")
        if avail_data:
            print(f"Minimum RAM Avail:  {min(avail_data)} MB")
            print(f"Average RAM Avail:  {sum(avail_data)/len(avail_data):.2f} MB")
            print(f"------------------------------------------\n")
    except Exception as e:
        print(f"Error analyzing RAM profile: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_ram.py <log_file>")
    else:
        analyze(sys.argv[1])
