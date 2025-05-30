#!/usr/bin/env python3
"""
Python syntax highlighting test for Monokai Spacegray Eighties theme
Tests: classes, functions, decorators, type hints, f-strings, comprehensions
"""

import asyncio
import pandas as pd
import numpy as np
from typing import List, Dict, Optional, Union, Callable
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataPoint:
    """A sample data point with various field types."""
    
    id: int
    value: float
    category: str
    is_valid: bool = True
    metadata: Optional[Dict[str, Union[str, int]]] = None


class DataProcessor:
    """Example class for data processing operations."""
    
    def __init__(self, config: Dict[str, any]) -> None:
        self.config = config
        self.data: List[DataPoint] = []
        self._processed = False
    
    @property
    def is_processed(self) -> bool:
        """Check if data has been processed."""
        return self._processed
    
    def add_data(self, points: List[DataPoint]) -> None:
        """Add data points to the processor."""
        self.data.extend(points)
        print(f"Added {len(points)} data points. Total: {len(self.data)}")
    
    @staticmethod
    def validate_point(point: DataPoint) -> bool:
        """Validate a single data point."""
        return (
            point.value >= 0 
            and point.category in ["A", "B", "C"]
            and isinstance(point.id, int)
        )
    
    async def process_async(self) -> Dict[str, float]:
        """Asynchronously process data points."""
        # Simulate async processing
        await asyncio.sleep(0.1)
        
        valid_points = [p for p in self.data if self.validate_point(p)]
        
        if not valid_points:
            raise ValueError("No valid data points found")
        
        # Calculate statistics using comprehensions
        stats = {
            "mean": sum(p.value for p in valid_points) / len(valid_points),
            "max": max(p.value for p in valid_points),
            "min": min(p.value for p in valid_points),
            "count": len(valid_points)
        }
        
        self._processed = True
        return stats


def create_sample_data(n: int = 100) -> List[DataPoint]:
    """Generate sample data points."""
    import random
    
    points = []
    for i in range(n):
        point = DataPoint(
            id=i,
            value=random.gauss(50, 15),
            category=random.choice(["A", "B", "C"]),
            is_valid=random.random() > 0.1,
            metadata={"source": f"generator_{i % 3}", "batch": i // 10}
        )
        points.append(point)
    
    return points


# Function with complex type hints
def analyze_data(
    data: List[DataPoint], 
    filter_func: Callable[[DataPoint], bool] = lambda x: x.is_valid,
    groupby: str = "category"
) -> pd.DataFrame:
    """Analyze data points and return summary statistics."""
    
    # Filter data
    filtered_data = list(filter(filter_func, data))
    
    # Convert to DataFrame
    df = pd.DataFrame([
        {
            "id": p.id,
            "value": p.value, 
            "category": p.category,
            "is_valid": p.is_valid
        }
        for p in filtered_data
    ])
    
    # Group and aggregate
    summary = df.groupby(groupby).agg({
        "value": ["mean", "std", "count"],
        "id": "max"
    }).round(2)
    
    return summary


# Example usage with f-strings and various operators
if __name__ == "__main__":
    # Create processor
    config = {
        "threshold": 25.0,
        "categories": ["A", "B", "C"],
        "validation": True
    }
    
    processor = DataProcessor(config)
    
    # Generate and add sample data
    sample_points = create_sample_data(n=50)
    processor.add_data(sample_points)
    
    # Process data synchronously for demo
    valid_data = [p for p in processor.data if processor.validate_point(p)]
    
    print(f"\nData Summary:")
    print(f"Total points: {len(processor.data)}")
    print(f"Valid points: {len(valid_data)}")
    print(f"Validation rate: {len(valid_data) / len(processor.data) * 100:.1f}%")
    
    # Category breakdown
    category_counts = {}
    for point in valid_data:
        category_counts[point.category] = category_counts.get(point.category, 0) + 1
    
    print(f"\nCategory breakdown:")
    for cat, count in sorted(category_counts.items()):
        percentage = count / len(valid_data) * 100
        print(f"  {cat}: {count:3d} ({percentage:5.1f}%)")
    
    # Analyze with pandas
    try:
        analysis = analyze_data(processor.data)
        print(f"\nStatistical Analysis:")
        print(analysis)
    except Exception as e:
        print(f"Analysis failed: {e}")
    
    # Demonstrate various Python operators and syntax
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers if x % 2 == 0]  # List comprehension
    even_squares = {x: x**2 for x in numbers if x % 2 == 0}  # Dict comprehension
    
    # String operations
    message = f"Processed {len(valid_data)} items"
    print(f"\n{message}")
    
    # Boolean operations
    has_data = len(processor.data) > 0
    is_complete = processor.is_processed and has_data
    
    print(f"Has data: {has_data}")
    print(f"Processing complete: {is_complete}")
    
    # Lambda and functional programming
    high_values = list(filter(lambda p: p.value > 60, valid_data))
    sorted_values = sorted(valid_data, key=lambda p: p.value, reverse=True)
    
    if high_values:
        top_value = max(high_values, key=lambda p: p.value)
        print(f"\nHighest value: {top_value.value:.2f} (Category: {top_value.category})")