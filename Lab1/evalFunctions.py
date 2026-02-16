import numpy as np

def calcAccuracy(LPred, LTrue):
    """Calculates prediction accuracy from data labels.

    Args:
        LPred (array): Predicted data labels.
        LTrue (array): Ground truth data labels.

    Returns:
        acc (float): Prediction accuracy.
    """

    # --------------------------------------------
    # === Your code here =========================
    # --------------------------------------------
    acc = float(np.mean(LPred == LTrue))
    # ============================================
    return acc


def calcConfusionMatrix(LPred, LTrue):
    """Calculates a confusion matrix from data labels.

    Args:
        LPred (array): Predicted data labels.
        LTrue (array): Ground truth data labels.

    Returns:
        cM (array): Confusion matrix, with predicted labels in the rows
            and actual labels in the columns.
    """

    # --------------------------------------------
    labels = np.unique(np.concatenate([LTrue, LPred])) 
    C = labels.size
    label_to_idx = {lab: i for i, lab in enumerate(labels)}

    cM = np.zeros((C, C), dtype=int)
    for p, t in zip(LPred, LTrue):
        cM[label_to_idx[p], label_to_idx[t]] += 1
    # --------------------------------------------
    # ============================================

    return cM


def calcAccuracyCM(cM):
    """Calculates prediction accuracy from a confusion matrix.

    Args:
        cM (array): Confusion matrix, with predicted labels in the rows
            and actual labels in the columns.

    Returns:
        acc (float): Prediction accuracy.
    """

    # --------------------------------------------
    correct = np.trace(cM)
    total = cM.sum()
    # --------------------------------------------
    acc = correct / total
    # ============================================
    
    return acc
