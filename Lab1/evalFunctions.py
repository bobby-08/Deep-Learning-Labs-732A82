import numpy as np

def calcAccuracy(LPred, LTrue):
    """Calculates prediction accuracy from data labels.

    Args:
        LPred (array): Predicted data labels.
        LTrue (array): Ground truth data labels.

    Retruns:
        acc (float): Prediction accuracy.
    """

    # --------------------------------------------
    # === Your code here =========================
    # --------------------------------------------
<<<<<<< HEAD
    acc = np.sum(LPred == LTrue) / len(LTrue)
=======
    acc = float(np.mean(LPred == LTrue))
>>>>>>> fd9afacc2ec881d051145b30117d032e391cb4aa
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
    # === Your code here =========================
    # --------------------------------------------
<<<<<<< HEAD
    classes = np.union1d(LPred, LTrue)
    K = len(classes)
    cM = np.zeros((K, K))
    for i in range(len(LTrue)):
        cM[LTrue[i], LPred[i]] += 1
=======
>>>>>>> fd9afacc2ec881d051145b30117d032e391cb4aa
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
    # === Your code here =========================
    # --------------------------------------------
<<<<<<< HEAD
    acc = np.sum(np.diag(cM)) / np.sum(cM)
=======
    acc = correct / total
>>>>>>> fd9afacc2ec881d051145b30117d032e391cb4aa
    # ============================================
    
    return acc
