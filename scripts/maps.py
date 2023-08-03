N1_PR_map = (
    "value",
    {
        "EXAMPLE INSURANCE COMPANY": (
            "value",
            {
                "XV": (
                    "value",
                    {
                        "88888": None
                    }
                )
            }
        )
    }
)

N1_PE_map = (
    "value",
    {
        "EXAMPLE MEDICAL CENTER": (
            "value",
            {
                "XX": (
                    "value",
                    {
                        "1234567890": None
                    }
                )
            }
        )
    }
)

N1_map = (
    "code",
    {
        "PR": N1_PR_map,
        "PE": N1_PE_map
    },
)

N3_map = (
    "value",
    {
        "123 MAIN ST": (
            "value", {
                "APT 1": None
            }
        )
    },
)

N4_map = (
    "value", {
        "SAN FRANCISCO": (
            "value", {
                "CA": (
                    "value", 
                    {
                        "94321": None
                    }
                )
            }
        )
    },
)

NM1_QC_1_map = (
    "value",
    {
        "MR": (
            "value",
            {
                "SMITH": (
                    "value",
                    {
                        "JOHN": (
                            "value",
                            {
                                "BEN": (
                                    "value",
                                    {
                                        "designation": (
                                            "value",
                                            {
                                                "MI": (
                                                    "value",
                                                    {
                                                        "123456789": None
                                                    }
                                                )
                                            }
                                        )
                                    }
                                )
                            }
                        )
                    }
                )
            }
        )
    }
)

NM1_74_1_map = (
    "value",
    {
        "DOE": (
            "value",
            {
                "JOHN": None
            }
        )
    }
)

NM1_map = (
    "code",
    {
        "QC": (
            "code", 
            {
                "1": NM1_QC_1_map
            }
        ),
        "74": (
            "code", 
            {
                "1": NM1_74_1_map
            }
        )
    }
)

PER_map = (
    "code", 
    {
        "BL": (
            "value",
            {
                "EXAMPLE SERVICES": (
                    "recursive_code", {
                        "UR": (
                            "value",
                            {
                                "WWW.EXAMPLE.ORG": None
                            }
                        )
                    }
                )
            }
        ),
        "CX": (
            "value",
            {
                "EXAMPLE SERVICES": (
                    "recursive_code", {
                        "TE": (
                            "value",
                            {
                                
                                "8001119999": None
                            }
                        ),
                    }
                )
            }
        )
    }
)

