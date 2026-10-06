
# ================================================================
# FEATURE CONFIGURATION
# ================================================================

FEATURES = {
    "study_hours": (
        "Study Hours Per Day",
        0.0,
        15.0,
        4.0,
        0.5,
        "Average number of hours the student studies per day."
    ),

    "attendance": (
        "Attendance Percentage",
        0.0,
        100.0,
        75.0,
        1.0,
        "Student attendance percentage."
    ),

    "previous_marks": (
        "Previous Examination Marks",
        0.0,
        100.0,
        65.0,
        1.0,
        "Marks obtained in the previous examination."
    ),

    "assignment_score": (
        "Assignment Score",
        0.0,
        100.0,
        70.0,
        1.0,
        "Average assignment score."
    ),

    "internal_marks": (
        "Internal Examination Marks",
        0.0,
        100.0,
        65.0,
        1.0,
        "Internal examination marks."
    ),

    "assignments_completed": (
        "Assignments Completed",
        0,
        20,
        10,
        1,
        "Number of assignments completed."
    ),

    "previous_failures": (
        "Previous Backlogs / Failures",
        0,
        10,
        0,
        1,
        "Number of previous failures or backlogs."
    ),

    "participation_score": (
        "Participation / Activity Score",
        0.0,
        100.0,
        70.0,
        1.0,
        "Class participation and academic activity score."
    ),
}


# List of feature names
FEATURE_NAMES = list(FEATURES.keys())


# User-friendly labels
FEATURE_LABELS = {
    key: value[0]
    for key, value in FEATURES.items()
}


# ================================================================
# PERFORMANCE CATEGORY STYLES
# ================================================================

CATEGORY_STYLE = {
    "Excellent": {
        "color": "#2E7D32",
        "icon": "🏆",
    },

    "Good": {
        "color": "#1565C0",
        "icon": "👍",
    },

    "Average": {
        "color": "#EF6C00",
        "icon": "📘",
    },

    "Poor": {
        "color": "#C62828",
        "icon": "⚠️",
    },
}


# ================================================================
# GET PERFORMANCE CATEGORY
# ================================================================

def get_category(score):
    """
    Convert the predicted score into a performance category.

    Categories:
        80 - 100 : Excellent
        60 - 79  : Good
        40 - 59  : Average
        0 - 39   : Poor
    """

    score = float(score)

    if score >= 80:
        return "Excellent"

    elif score >= 60:
        return "Good"

    elif score >= 40:
        return "Average"

    else:
        return "Poor"


# ================================================================
# GET PERFORMANCE MESSAGE
# ================================================================

def get_message(category):
    """
    Return a message based on the student's performance category.
    """

    messages = {
        "Excellent": (
            "Excellent performance! Keep maintaining your "
            "study habits, attendance, and academic consistency."
        ),

        "Good": (
            "Good performance! You can improve further by "
            "increasing study hours and maintaining strong attendance."
        ),

        "Average": (
            "Your performance is average. Focus on improving "
            "your study routine, attendance, assignments, and internal marks."
        ),

        "Poor": (
            "Your predicted performance needs improvement. "
            "Create a consistent study schedule and seek academic "
            "support when needed."
        ),
    }

    return messages.get(
        category,
        "Keep working consistently toward your academic goals."
    )


# ================================================================
# GET PERSONALIZED RECOMMENDATIONS
# ================================================================

def get_recommendations(inputs):
    """
    Generate personalized recommendations based on
    the student's input values.
    """

    recommendations = []

    # Study hours
    if inputs["study_hours"] < 3:
        recommendations.append(
            "📚 Increase your daily study time to at least "
            "3–4 focused hours."
        )

    # Attendance
    if inputs["attendance"] < 75:
        recommendations.append(
            "⚠️ Improve your attendance. Try to maintain "
            "at least 75% attendance."
        )

    # Previous marks
    if inputs["previous_marks"] < 50:
        recommendations.append(
            "📖 Revise previous topics and strengthen "
            "your basic concepts."
        )

    # Assignment score
    if inputs["assignment_score"] < 60:
        recommendations.append(
            "📝 Spend more time on assignments and "
            "submit them regularly."
        )

    # Internal marks
    if inputs["internal_marks"] < 50:
        recommendations.append(
            "✍️ Prepare regularly for internal examinations."
        )

    # Assignments completed
    if inputs["assignments_completed"] < 8:
        recommendations.append(
            "📋 Try to complete more assignments on time."
        )

    # Previous failures
    if inputs["previous_failures"] > 0:
        recommendations.append(
            "🎯 Give extra attention to subjects where "
            "you previously struggled."
        )

    # Participation
    if inputs["participation_score"] < 50:
        recommendations.append(
            "🙋 Participate more actively in classes "
            "and academic activities."
        )

    # If everything is good
    if not recommendations:
        recommendations.append(
            "🌟 Your academic indicators look strong. "
            "Keep maintaining your current routine!"
        )

    return recommendations


# ================================================================
# GET STUDENT STRENGTHS
# ================================================================

def get_strengths(inputs):
    """
    Identify the student's strongest academic indicators.
    """

    strengths = []

    if inputs["study_hours"] >= 5:
        strengths.append(
            "Good study routine"
        )

    if inputs["attendance"] >= 85:
        strengths.append(
            "Excellent attendance"
        )

    if inputs["previous_marks"] >= 75:
        strengths.append(
            "Strong previous marks"
        )

    if inputs["assignment_score"] >= 75:
        strengths.append(
            "Good assignment performance"
        )

    if inputs["internal_marks"] >= 75:
        strengths.append(
            "Strong internal marks"
        )

    if inputs["participation_score"] >= 75:
        strengths.append(
            "Good participation"
        )

    return strengths
