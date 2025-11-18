#!/usr/bin/env python3
"""
Calculate and update model performance statistics
"""
import json
from datetime import datetime

def calculate_performance():
    """Calculate overall model performance"""
    try:
        with open('data/predictions_history.json', 'r') as f:
            predictions = json.load(f)
    except FileNotFoundError:
        predictions = []
    
    # Filter checked predictions
    checked = [p for p in predictions if p.get('result_checked')]
    
    if not checked:
        performance = {
            "status": "NEW MODEL",
            "message": "Tracking starts today - check back after games complete"
        }
    else:
        total = len(checked)
        correct = sum(1 for p in checked if p.get('was_correct'))
        accuracy = (correct / total * 100) if total > 0 else 0
        
        # By confidence level
        high_conf = [p for p in checked if p.get('confidence', 0) >= 70]
        high_conf_correct = sum(1 for p in high_conf if p.get('was_correct'))
        high_conf_acc = (high_conf_correct / len(high_conf) * 100) if high_conf else 0
        
        performance = {
            "last_updated": datetime.now().isoformat(),
            "total_predictions": total,
            "correct": correct,
            "incorrect": total - correct,
            "accuracy_percent": round(accuracy, 1),
            "by_confidence": {
                "high_70plus": {
                    "total": len(high_conf),
                    "correct": high_conf_correct,
                    "accuracy": round(high_conf_acc, 1)
                }
            },
            "status": "LIVE TRACKING"
        }
    
    # Save performance stats
    with open('data/performance.json', 'w') as f:
        json.dump(performance, f, indent=2)
    
    print(f"✅ Performance updated: {performance.get('accuracy_percent', 'N/A')}% accurate")

if __name__ == "__main__":
    calculate_performance()
