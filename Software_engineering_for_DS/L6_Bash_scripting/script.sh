#!/bin/bash
# Project Release Build Script - Enhanced Version
# Copies files from source to build directory with robust error handling

echo "🚀 Welcome to the Project Release Builder! 🛠️"
echo "============================================"
echo ""

# ========================
# ENHANCEMENT: Better error checking
# ========================

# Verify required directories exist
if [ ! -d "source" ]; then
  echo "❌ Error: 'source' directory not found!"
  exit 1
fi

if [ ! -d "build" ]; then
  echo "⚠️ Warning: 'build' directory not found, creating it..."
  mkdir build || { echo "❌ Failed to create build directory"; exit 1; }
fi

# ========================
# ENHANCEMENT: Changelog validation
# ========================
if [ ! -f "source/changelog.md" ] || [ ! -s "source/changelog.md" ]; then
  echo "❌ Error: changelog.md is missing or empty!"
  exit 1
fi

firstline=$(head -n 1 source/changelog.md)
read -a splitfirstline <<< "$firstline"

if [ ${#splitfirstline[@]} -lt 2 ]; then
  echo "❌ Error: Invalid format in changelog.md"
  exit 1
fi

version=${splitfirstline[1]}

echo "📦 You are building version: $version"
echo "⏱️  Build started at: $(date)"
echo ""

# ========================
# ENHANCEMENT: Robust user input handling
# ========================
while true; do
  read -p "Do you want to continue with the build? (1 for yes, 0 for no): " userConfirmation
  
  case $userConfirmation in
    [1])
      echo "✅ Proceeding with build..."
      break
      ;;
    [0])
      echo "🛑 Build canceled. Please come back when you're ready."
      exit 0
      ;;
    *)
      echo "❌ Invalid input. Please enter 1 for yes or 0 for no."
      ;;
  esac
done

# ========================
# ENHANCEMENT: Conditional cleaning
# ========================
if [ "$(ls -A build 2>/dev/null)" ]; then
  echo "🧹 Cleaning build directory..."
  if ! rm -rf build/*; then
    echo "❌ Failed to clean build directory"
    exit 1
  fi
fi

# Process each file
for filename in source/*
do
  echo "🔍 Processing: $(basename "$filename")"
  
  # ========================
  # ENHANCEMENT: Better case statement formatting
  # ========================
  case $(basename "$filename") in
    secretinfo.md)
      echo "   🔒 Sanitizing secretinfo.md"
      if ! sed 's/42/XX/g' "source/secretinfo.md" > "build/secretinfo.md"; then
        echo "❌ Failed to process secretinfo.md"
        exit 1
      fi
      ;;
    *)
      echo "   📄 Copying $(basename "$filename")"
      if ! cp "$filename" build/; then
        echo "❌ Failed to copy $filename"
        exit 1
      fi
      ;;
  esac
done

# List build contents
echo ""
echo "📋 Build $version completed. Contents:"
if ! ls -lh build/; then
  echo "❌ Failed to list build directory contents"
  exit 1
fi

echo ""
echo "✨ Build successful! 🎉"
exit 0