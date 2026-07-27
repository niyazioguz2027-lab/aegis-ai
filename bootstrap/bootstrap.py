#!/usr/bin/env python3
"""AEGIS Enterprise Monorepo Bootstrap Generator."""

import sys
from pathlib import Path

from generators.project_generator import ProjectGenerator

def main() -> int:
    """Bootstrap AEGIS enterprise monorepo structure."""
    root = Path.cwd()
    
    try:
        print("🚀 AEGIS Bootstrap - Enterprise Monorepo Generator\n")
        print("=" * 60)
        
        generator = ProjectGenerator(root)
        generator.generate()
        
        print("\n" + "=" * 60)
        print("✅ Bootstrap complete!")
        print("\nNext steps:")
        print("  1. cd aegis-ai")
        print("  2. make install")
        print("  3. make pre-commit")
        print("  4. make docker-up")
        print("  5. make test")
        
        return 0
    except Exception as e:
        print(f"\n❌ Bootstrap failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
