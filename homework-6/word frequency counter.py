import string
import os
from collections import Counter
import re

def word_frequency_counter():
    """
    Enhanced Word Frequency Counter with user-specified top words display,
    improved efficiency, and comprehensive error handling.
    """
    
    # Get input file from user
    filename = get_input_filename()
    if not filename:
        return
    
    # Get number of top words to display
    top_n = get_top_n_words()
    if not top_n:
        return
    
    # Process the file
    try:
        word_counts, total_words = process_file(filename)
        
        if total_words == 0:
            print("No words found in the file.")
            return
        
        # Get top N words
        top_words = word_counts.most_common(top_n)
        
        # Display results
        display_results(top_words, total_words, top_n)
        
        # Save report
        save_report(top_words, total_words, top_n, filename)
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_input_filename():
    """Get and validate input filename from user"""
    while True:
        try:
            filename = input("Enter the filename to analyze (or press Enter for 'sample.txt'): ").strip()
            
            # Use default if no input
            if not filename:
                filename = "sample.txt"
            
            # Check if file exists
            if not os.path.exists(filename):
                print(f"Error: File '{filename}' not found.")
                retry = input("Would you like to try another filename? (y/n): ").strip().lower()
                if retry != 'y':
                    return None
                continue
            
            # Check if file is readable
            try:
                with open(filename, 'r', encoding='utf-8') as test_file:
                    test_file.read(1)  # Try to read one character
                return filename
            except UnicodeDecodeError:
                print(f"Error: Cannot read '{filename}'. File might be binary or use unsupported encoding.")
                retry = input("Would you like to try another filename? (y/n): ").strip().lower()
                if retry != 'y':
                    return None
                continue
            except PermissionError:
                print(f"Error: Permission denied to read '{filename}'.")
                retry = input("Would you like to try another filename? (y/n): ").strip().lower()
                if retry != 'y':
                    return None
                continue
                
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None

def get_top_n_words():
    """Get number of top words to display from user"""
    while True:
        try:
            user_input = input("Enter number of top words to display (default: 5): ").strip()
            
            # Use default if no input
            if not user_input:
                return 5
            
            # Validate input
            top_n = int(user_input)
            if top_n <= 0:
                print("Please enter a positive number.")
                continue
            
            if top_n > 1000:
                confirm = input(f"You requested {top_n} words. This might be a lot. Continue? (y/n): ").strip().lower()
                if confirm != 'y':
                    continue
            
            return top_n
            
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None

def process_file(filename):
    """
    Process the file and return word counts and total word count.
    Uses Counter for efficiency and improved text processing.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Handle empty file
        if not text.strip():
            return Counter(), 0
        
        # More robust word extraction using regex
        # This handles various punctuation and keeps contractions intact
        words = re.findall(r"\b[a-zA-Z]+(?:[''][a-zA-Z]+)?\b", text.lower())
        
        # Alternative method using string translation (your original approach, but improved)
        # text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
        # words = text_no_punct.lower().split()
        
        # Filter out very short words (optional - can be made configurable)
        words = [word for word in words if len(word) > 1]
        
        # Use Counter for efficient counting
        word_counts = Counter(words)
        
        return word_counts, len(words)
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return Counter(), 0
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        return Counter(), 0
    except UnicodeDecodeError:
        print(f"Error: Cannot decode '{filename}'. File might use unsupported encoding.")
        return Counter(), 0
    except MemoryError:
        print("Error: File is too large to process in memory.")
        return Counter(), 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return Counter(), 0

def display_results(top_words, total_words, top_n):
    """Display the word frequency results"""
    print(f"\n{'='*50}")
    print(f"WORD FREQUENCY ANALYSIS RESULTS")
    print(f"{'='*50}")
    print(f"Total words: {total_words:,}")
    print(f"Unique words: {len(top_words) if len(top_words) < top_n else 'Many'}")
    print(f"\nTop {min(top_n, len(top_words))} most common words:")
    print(f"{'-'*30}")
    
    for i, (word, count) in enumerate(top_words, 1):
        percentage = (count / total_words) * 100
        print(f"{i:2d}. {word:<15} - {count:>4} ({percentage:.1f}%)")

def save_report(top_words, total_words, top_n, source_filename):
    """Save the word frequency report to a file"""
    try:
        report_filename = "word_count_report.txt"
        
        with open(report_filename, 'w', encoding='utf-8') as report_file:
            report_file.write("WORD FREQUENCY ANALYSIS REPORT\n")
            report_file.write("=" * 50 + "\n")
            report_file.write(f"Source file: {source_filename}\n")
            report_file.write(f"Analysis date: {get_current_datetime()}\n")
            report_file.write(f"Total words: {total_words:,}\n")
            report_file.write(f"Unique words found: {len(top_words) if len(top_words) < top_n else 'Many'}\n")
            report_file.write(f"\nTop {min(top_n, len(top_words))} most common words:\n")
            report_file.write("-" * 40 + "\n")
            
            for i, (word, count) in enumerate(top_words, 1):
                percentage = (count / total_words) * 100
                report_file.write(f"{i:2d}. {word:<15} - {count:>4} ({percentage:.1f}%)\n")
            
            report_file.write("\n" + "=" * 50 + "\n")
            report_file.write("End of report\n")
        
        print(f"\nReport saved to '{report_filename}' ✅")
        
    except PermissionError:
        print("Error: Permission denied to save report file.")
    except Exception as e:
        print(f"Error saving report: {e}")

def get_current_datetime():
    """Get current date and time as string"""
    try:
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    except:
        return "Unknown"

def process_large_file(filename, top_n):
    """
    Alternative method for processing very large files that might not fit in memory.
    This is a more memory-efficient approach for huge files.
    """
    try:
        word_counts = Counter()
        total_words = 0
        
        with open(filename, 'r', encoding='utf-8') as file:
            # Process file in chunks
            chunk_size = 1024 * 1024  # 1MB chunks
            
            leftover = ""
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                
                # Handle word boundaries at chunk edges
                chunk = leftover + chunk
                words = re.findall(r"\b[a-zA-Z]+(?:[''][a-zA-Z]+)?\b", chunk.lower())
                
                # Keep last word for next chunk (might be incomplete)
                if chunk and not chunk[-1].isspace():
                    leftover = words[-1] if words else ""
                    words = words[:-1] if words else []
                else:
                    leftover = ""
                
                # Filter short words
                words = [word for word in words if len(word) > 1]
                
                # Update counters
                word_counts.update(words)
                total_words += len(words)
        
        return word_counts, total_words
        
    except Exception as e:
        print(f"Error processing large file: {e}")
        return Counter(), 0

def main():
    """Main function to run the word frequency counter"""
    print("Welcome to the Enhanced Word Frequency Counter!")
    print("=" * 50)
    
    while True:
        try:
            word_frequency_counter()
            
            # Ask if user wants to analyze another file
            another = input("\nWould you like to analyze another file? (y/n): ").strip().lower()
            if another != 'y':
                break
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
    
    print("Thank you for using the Word Frequency Counter!")

if __name__ == "__main__":
    main()