{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "\n",
        "#a) Load the iris dataset, print its shape and display the first 5 entries"
      ],
      "metadata": {
        "id": "Ecn3GQ5OlWhZ"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "z9RRafXej5KS",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "388e9807-fa38-4a30-9ae2-4bf8c603444a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(150, 5)\n",
            "   sepal.length  sepal.width  petal.length  petal.width variety\n",
            "0           5.1          3.5           1.4          0.2  Setosa\n",
            "1           4.9          3.0           1.4          0.2  Setosa\n",
            "2           4.7          3.2           1.3          0.2  Setosa\n",
            "3           4.6          3.1           1.5          0.2  Setosa\n",
            "4           5.0          3.6           1.4          0.2  Setosa\n"
          ]
        }
      ],
      "source": [
        "# Use pandas.read_csv to load the iris.csv file into a dataframe called \"data\"\n",
        "# Print the shape of the dataframe\n",
        "# Print the first 5 entries of the dataframe\n",
        "import pandas as pd\n",
        "df = pd.read_csv(\"/content/drive/MyDrive/IIS/iris.csv\")\n",
        "print(df.shape)# Print the shape of the dataframe\n",
        "print(df.head(5))# Print the first 5 entries of the dataframe\n",
        "# Enter code here"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "#b) Print the column information of the data-frame"
      ],
      "metadata": {
        "id": "oNhct_XMliYq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# print the column information of the dataframe\n",
        "print(df.info())\n",
        "# Enter code here"
      ],
      "metadata": {
        "id": "MoaSBn0Uk905",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1a1fb2d0-7a1f-4efd-ef45-66d424948f64"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 150 entries, 0 to 149\n",
            "Data columns (total 5 columns):\n",
            " #   Column        Non-Null Count  Dtype  \n",
            "---  ------        --------------  -----  \n",
            " 0   sepal.length  150 non-null    float64\n",
            " 1   sepal.width   150 non-null    float64\n",
            " 2   petal.length  150 non-null    float64\n",
            " 3   petal.width   150 non-null    float64\n",
            " 4   variety       150 non-null    object \n",
            "dtypes: float64(4), object(1)\n",
            "memory usage: 6.0+ KB\n",
            "None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#c) Visualize the class distribution using a bar graph."
      ],
      "metadata": {
        "id": "qKTEtpKyk5CJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Use np.unique() to find the count of each unique entry of the variety column\n",
        "import numpy as np\n",
        "\n",
        "uv, c = np.unique(variety, return_counts=True)\n",
        "\n",
        "# Enter code here"
      ],
      "metadata": {
        "id": "lGp82rYhmdqk",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 536
        },
        "outputId": "97bef543-20a8-4aa9-81be-de7daf137ea5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-10-b370f1719ec0>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mmatplotlib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpyplot\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0ma\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0munique\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;31m# Enter code here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/numpy/core/overrides.py\u001b[0m in \u001b[0;36munique\u001b[0;34m(*args, **kwargs)\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/numpy/lib/arraysetops.py\u001b[0m in \u001b[0;36munique\u001b[0;34m(ar, return_index, return_inverse, return_counts, axis)\u001b[0m\n\u001b[1;32m    270\u001b[0m     \u001b[0mar\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0masanyarray\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mar\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    271\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0maxis\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 272\u001b[0;31m         \u001b[0mret\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_unique1d\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mar\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreturn_index\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreturn_inverse\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreturn_counts\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    273\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0m_unpack_tuple\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mret\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    274\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/numpy/lib/arraysetops.py\u001b[0m in \u001b[0;36m_unique1d\u001b[0;34m(ar, return_index, return_inverse, return_counts)\u001b[0m\n\u001b[1;32m    331\u001b[0m         \u001b[0maux\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mar\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mperm\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    332\u001b[0m     \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 333\u001b[0;31m         \u001b[0mar\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msort\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    334\u001b[0m         \u001b[0maux\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mar\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    335\u001b[0m     \u001b[0mmask\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mempty\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0maux\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdtype\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbool_\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: '<' not supported between instances of 'str' and 'float'"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#d) Make distribution plots for all the 4 features."
      ],
      "metadata": {
        "id": "f532UnEmnruC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Use plt.histogram() to plot the distribution of all the 4 input features\n",
        "# Enter code here for sepal.length\n",
        "import pandas as pd\n",
        "\n",
        "df = pd.read_csv(\"/content/drive/MyDrive/IIS/iris.csv\")\n",
        "plt.hist(df['sepal.length'])"
      ],
      "metadata": {
        "id": "_VG_zshjnqgF",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 317
        },
        "outputId": "e98f7cf4-2214-464b-f2a9-40613a6febec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(array([ 9., 23., 14., 27., 16., 26., 18.,  6.,  5.,  6.]),\n",
              " array([4.3 , 4.66, 5.02, 5.38, 5.74, 6.1 , 6.46, 6.82, 7.18, 7.54, 7.9 ]),\n",
              " <BarContainer object of 10 artists>)"
            ]
          },
          "metadata": {},
          "execution_count": 21
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Enter code here for sepal.width\n",
        "plt.hist(df['sepal.width'])"
      ],
      "metadata": {
        "id": "cEE11iKFMq9P",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 317
        },
        "outputId": "005c2377-3474-482d-a7ab-7c924c0a0855"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(array([ 4.,  7., 22., 24., 37., 31., 10., 11.,  2.,  2.]),\n",
              " array([2.  , 2.24, 2.48, 2.72, 2.96, 3.2 , 3.44, 3.68, 3.92, 4.16, 4.4 ]),\n",
              " <BarContainer object of 10 artists>)"
            ]
          },
          "metadata": {},
          "execution_count": 24
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Enter code here for petal.length\n",
        "plt.hist(df['petal.length'])"
      ],
      "metadata": {
        "id": "PMyO4MXnMxHG",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 317
        },
        "outputId": "2792c189-3e8c-4561-da92-84cd57636e45"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(array([37., 13.,  0.,  3.,  8., 26., 29., 18., 11.,  5.]),\n",
              " array([1.  , 1.59, 2.18, 2.77, 3.36, 3.95, 4.54, 5.13, 5.72, 6.31, 6.9 ]),\n",
              " <BarContainer object of 10 artists>)"
            ]
          },
          "metadata": {},
          "execution_count": 23
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Enter code here for petal.width\n",
        "plt.hist(df['petal.width'])"
      ],
      "metadata": {
        "id": "Lrio5I34M3LI",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 317
        },
        "outputId": "2b3b5b08-34f0-474e-cf24-a66329e56eaa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(array([41.,  8.,  1.,  7.,  8., 33.,  6., 23.,  9., 14.]),\n",
              " array([0.1 , 0.34, 0.58, 0.82, 1.06, 1.3 , 1.54, 1.78, 2.02, 2.26, 2.5 ]),\n",
              " <BarContainer object of 10 artists>)"
            ]
          },
          "metadata": {},
          "execution_count": 22
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#e) Mean and Standard Deviation of all the 4 features"
      ],
      "metadata": {
        "id": "oOG_kbF6nyf9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Use dataframe.mean() and dataframe.std() to print the mean and standard deviation for all the input features\n",
        "\n",
        "# Enter code here for sepal.length\n",
        "df = pd.read_csv(\"/content/drive/MyDrive/IIS/iris.csv\")\n",
        "x=df['sepal.length'].mean()\n",
        "y =df['sepal.length'].std()\n",
        "print(x)\n",
        "print(y)"
      ],
      "metadata": {
        "id": "9SIrq7uHnlur",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ee84181d-3633-4883-a906-37fae41553d7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5.843333333333334\n",
            "0.828066127977863\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Enter code here for sepal.width\n",
        "df = pd.read_csv(\"/content/drive/MyDrive/IIS/iris.csv\")\n",
        "q=df['sepal.width'].mean()\n",
        "w =df['sepal.width'].std()\n",
        "print(q)\n",
        "print(w)"
      ],
      "metadata": {
        "id": "nHs0IskiNWex",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1675e2bb-7d13-4270-8ec1-18e821076119"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.0573333333333337\n",
            "0.4358662849366982\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Enter code here for petal.length\n",
        "df = pd.read_csv(\"/content/drive/MyDrive/IIS/iris.csv\")\n",
        "e=df['petal.length'].mean()\n",
        "r =df['petal.length'].std()\n",
        "print(e)\n",
        "print(w)"
      ],
      "metadata": {
        "id": "xoAUb0FENbj-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c1babbdd-af06-4503-a9d4-152ed98fe25b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.7580000000000005\n",
            "0.4358662849366982\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Enter code here for petal.width\n",
        "df = pd.read_csv(\"/content/drive/MyDrive/IIS/iris.csv\")\n",
        "d=df['petal.length'].mean()\n",
        "f =df['petal.length'].std()\n",
        "print(d)\n",
        "print(f)"
      ],
      "metadata": {
        "id": "lxSZPdDRNgO8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "55f83b53-e517-4806-e9c2-a87a031d93f8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.7580000000000005\n",
            "1.7652982332594662\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#f) Correlation among the features."
      ],
      "metadata": {
        "id": "XugT57rWoRhi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Use np.corrcoef to compute the 4x4 correlation matrix for the input features\n",
        "# Hint - You need to pass rowvar=False as an additional parameter to the np.corrcoef\n",
        "# Enter code here\n",
        "import numpy as np\n",
        "m=['sepal.length','sepal.width','petal.length','petal.width']\n",
        "print(np.corrcoef(df[m].values,rowvar=False))"
      ],
      "metadata": {
        "id": "KQ7xiLcUob_p",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6383f6c9-0770-4df6-a5b3-07c5c14d07aa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[ 1.         -0.11756978  0.87175378  0.81794113]\n",
            " [-0.11756978  1.         -0.4284401  -0.36612593]\n",
            " [ 0.87175378 -0.4284401   1.          0.96286543]\n",
            " [ 0.81794113 -0.36612593  0.96286543  1.        ]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# comment on the features that you think are correlated\n",
        "#diagonal entries of all matrix are equal to 1 therefore all are related to each in some way"
      ],
      "metadata": {
        "id": "Z2RWeYfBN6lo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#g) Pairwise scatter plots"
      ],
      "metadata": {
        "id": "lj__jZXsoeor"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Use plt.scatter to build the scatter plots for various pairs of features\n",
        "# Use the colors list as a parameter for the scatter function to define the colors for the scatter plot\n",
        "color_dict = { 'Setosa':'red', 'Versicolor':'blue', 'Virginica':'green' }\n",
        "colors = [color_dict[i] for i in df['variety']]\n",
        "# Enter code here for sepal.length and sepal.width"
      ],
      "metadata": {
        "id": "TVijpY8oo3bG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "color_dict = { 'Setosa':'red', 'Versicolor':'blue', 'Virginica':'green' }\n",
        "colors = [color_dict[i] for i in df['variety']]\n",
        "\n",
        "# Scatter plot for sepal.length and sepal.width\n",
        "plt.scatter(df['sepal.length'], df['sepal.width'], c=colors)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "Y9jyXrcjOXIW",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "3b1d9701-96fe-4bd3-e55f-d8e13d06f32e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Enter code here for sepal.length and petal.width\n",
        "color_dict = { 'Setosa':'red', 'Versicolor':'blue', 'Virginica':'green' }\n",
        "colors = [color_dict[i] for i in df['variety']]\n",
        "\n",
        "# Scatter plot for sepal.length and sepal.width\n",
        "plt.scatter(df['sepal.length'], df['sepal.width'], c=colors)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "LT0nxJSKOcDe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Enter code here for sepal.width and petal.length\n",
        "color_dict = { 'Setosa':'red', 'Versicolor':'blue', 'Virginica':'green' }\n",
        "colors = [color_dict[i] for i in df['variety']]\n",
        "\n",
        "plt.scatter(df['sepal.length'], df['petal.length'], c=colors)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "-AvoJuI_Oe5Q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Enter code here for sepal.width and petal.width\n",
        "color_dict = { 'Setosa':'red', 'Versicolor':'blue', 'Virginica':'green' }\n",
        "colors = [color_dict[i] for i in df['variety']]\n",
        "\n",
        "#plt.scatter(df['sepal.length'], df['petal.length'], c=colors)\n",
        "plt.scatter(df['sepal.width'], df['petal.length'], c=colors)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "33uS18vnOoSw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Enter code here for petal.length and petal.width\n",
        "color_dict = { 'Setosa':'red', 'Versicolor':'blue', 'Virginica':'green' }\n",
        "colors = [color_dict[i] for i in df['variety']]\n",
        "plt.scatter(df['petal.lenfth'], df['petal.width'], c=colors)\n",
        "plt.show()\n"
      ],
      "metadata": {
        "id": "B9cHkHZXOrzW"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}