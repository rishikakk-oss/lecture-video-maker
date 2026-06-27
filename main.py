import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Lecture Video Maker CLI")
    parser.add_argument('--input', type=str, help='Input file (e.g., markdown script)')
    parser.add_argument('--output', type=str, default='output.mp4', help='Output video file name')
    
    args = parser.parse_args()
    
    if not args.input:
        parser.print_help()
        sys.exit(1)
        
    print(f"Starting video generation for {args.input}...")
    print(f"Output will be saved to {args.output}")
    # TODO: Initialize video generation pipeline here
    
if __name__ == '__main__':
    main()
